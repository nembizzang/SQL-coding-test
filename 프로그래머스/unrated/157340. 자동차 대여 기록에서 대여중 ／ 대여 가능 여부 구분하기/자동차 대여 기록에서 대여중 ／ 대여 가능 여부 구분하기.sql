SELECT DISTINCT(car_id) CAR_ID
       , IF(car_id IN (SELECT car_id
                         FROM car_rental_company_rental_history
                        WHERE '2022-10-16' BETWEEN start_date and end_date),
            '대여중','대여 가능') AVAILABILITY
    FROM car_rental_company_rental_history
    ORDER BY CAR_ID DESC;