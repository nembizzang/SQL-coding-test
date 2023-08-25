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