# output : c.car_id, c.car_type, fee((DATEDIFF(h.end_date,h.start_date)+1)*c.daily_fee*d.discount_rate(대여일에 따라 d.duration_type에 맞는 d.discount_rate 입력)
# 조건 : c.car_type IN ('세단','SUV'), h.end_date < '2022-11-01' OR h.start_date < '2022-11-30', fee BETWEEN(50,200)
# alias : car_rental_company_car c, car_rental_company_rental_history h, car_rental_company_discount_plan d
# JOIN KEY : c.car_id = h.car_id / c.car_type = d.car_type

SELECT f.car_id, f.car_type, ROUND(30*f.daily_fee*(100-discount_rate)/100) fee
    FROM  (SELECT car_id, car_type, daily_fee
            FROM car_rental_company_car
            WHERE car_id IN (SELECT car_id
                                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                GROUP BY car_id
                                HAVING COUNT(car_id) = SUM((CASE WHEN end_date < '2022-11-01' OR start_date > '2022-11-30' THEN 1
                                                                 ELSE 0
                                                            END)))
                 AND car_type IN ('세단','SUV')) f
    INNER JOIN car_rental_company_discount_plan d
            ON f.car_type = d.car_type
    WHERE d.duration_type = '30일 이상'
    HAVING fee BETWEEN 500000 AND 2000000
    ORDER BY fee DESC, car_type, car_id DESC;
