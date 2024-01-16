# 1. history로 duration, duration_type 구하기
SELECT history_id, car_id, DATEDIFF(end_date,start_date)+1 duration,
        (CASE WHEN DATEDIFF(end_date,start_date)+1 >= 90 THEN '90일 이상'
            WHEN DATEDIFF(end_date,start_date)+1 >= 30 THEN '30일 이상'
            WHEN DATEDIFF(end_date,start_date)+1 >= 7 THEN '7일 이상'
            ELSE NULL
            END) duration_type
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY;

# 2. car_id에 맞는 car_type과 daily_fee 붙이기
SELECT h.history_id, c.car_id, h.duration, h.duration_type, c.daily_fee, c.car_type
    FROM CAR_RENTAL_COMPANY_CAR c
    JOIN (SELECT history_id, car_id, DATEDIFF(end_date,start_date)+1 duration,
            (CASE WHEN DATEDIFF(end_date,start_date)+1 >= 90 THEN '90일 이상'
                WHEN DATEDIFF(end_date,start_date)+1 >= 30 THEN '30일 이상'
                WHEN DATEDIFF(end_date,start_date)+1 >= 7 THEN '7일 이상'
                ELSE NULL
                END) duration_type
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) h
      ON c.car_id = h.car_id;

# 3. car_type과 duration_type에 맞는 duration_rate 붙이기
SELECT ch.history_id, ch.car_id, ch.duration, ch.duration_type, ch.daily_fee, ch.car_type, p.discount_rate
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    JOIN (SELECT h.history_id, c.car_id, h.duration, h.duration_type, c.daily_fee, c.car_type
            FROM CAR_RENTAL_COMPANY_CAR c
            JOIN (SELECT history_id, car_id, DATEDIFF(end_date,start_date)+1 duration,
                    (CASE WHEN DATEDIFF(end_date,start_date)+1 >= 90 THEN '90일 이상'
                        WHEN DATEDIFF(end_date,start_date)+1 >= 30 THEN '30일 이상'
                        WHEN DATEDIFF(end_date,start_date)+1 >= 7 THEN '7일 이상'
                        ELSE NULL
                        END) duration_type
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) h
              ON c.car_id = h.car_id) ch
      ON p.car_type = ch.car_type AND p.duration_type = ch.duration_type;
      
# 4. fee 계산
SELECT chp.history_id, ROUND(daily_fee*duration*(100-discount_rate)/100) fee
    FROM (SELECT ch.history_id, ch.car_id, ch.duration, ch.duration_type, ch.daily_fee, ch.car_type, p.discount_rate
            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
            JOIN (SELECT h.history_id, c.car_id, h.duration, h.duration_type, c.daily_fee, c.car_type
                    FROM CAR_RENTAL_COMPANY_CAR c
                    JOIN (SELECT history_id, car_id, DATEDIFF(end_date,start_date)+1 duration,
                            (CASE WHEN DATEDIFF(end_date,start_date)+1 >= 90 THEN '90일 이상'
                                WHEN DATEDIFF(end_date,start_date)+1 >= 30 THEN '30일 이상'
                                WHEN DATEDIFF(end_date,start_date)+1 >= 7 THEN '7일 이상'
                                ELSE NULL
                                END) duration_type
                        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) h
                      ON c.car_id = h.car_id) ch
              ON p.car_type = ch.car_type AND p.duration_type = ch.duration_type) chp
    WHERE car_type='트럭'
    ORDER BY fee DESC, history_id DESC;
      






SELECT d.history_id, ROUND(d.duration*d.daily_fee*(100-IFNULL(p.discount_rate,0))/100) fee
    FROM (SELECT r.history_id, r.car_id, r.daily_fee, r.duration, r.car_type,
                (CASE WHEN r.duration < 7 THEN NULL
                      WHEN r.duration BETWEEN 7 AND 29 THEN '7일 이상'
                      WHEN r.duration BETWEEN 30 AND 89 THEN '30일 이상'
                      ELSE '90일 이상'
                 END) duration_type
            FROM (SELECT h.history_id, c.car_id, c.car_type, c.daily_fee, DATEDIFF(h.end_date, h.start_date)+1 duration
                    FROM car_rental_company_car c
                    INNER JOIN car_rental_company_rental_history h
                            ON c.car_id = h.car_id
                  WHERE c.car_type = '트럭'
                 ) r
         ) d
    LEFT OUTER JOIN car_rental_company_discount_plan p
                 ON d.duration_type = p.duration_type AND d.car_type = p.car_type
    ORDER BY fee DESC, history_id DESC;