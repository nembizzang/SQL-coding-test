SELECT DISTINCT(c.car_id)
    FROM car_rental_company_car c
    LEFT OUTER JOIN car_rental_company_rental_history h
                ON c.car_id = h.car_id
    WHERE c.car_type = '세단' AND MONTH(h.start_date) = 10
    ORDER BY c.car_id DESC; 
















# SELECT DISTINCT(car.car_id)
#     FROM car_rental_company_car car
#     LEFT OUTER JOIN car_rental_company_rental_history history
#                 ON car.car_id = history.car_id
#     WHERE car.car_type = '세단' AND MONTH(history.start_date) = 10
#     ORDER BY car.car_id DESC;