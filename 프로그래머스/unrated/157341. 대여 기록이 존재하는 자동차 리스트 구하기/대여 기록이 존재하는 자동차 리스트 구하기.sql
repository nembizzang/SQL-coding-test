SELECT DISTINCT(car.car_id)
    FROM car_rental_company_car car
    LEFT OUTER JOIN car_rental_company_rental_history history
                ON car.car_id = history.car_id
    WHERE car.car_type = '세단' AND MONTH(history.start_date) = 10
    ORDER BY car.car_id DESC;