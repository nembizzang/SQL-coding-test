SELECT ROUND(AVG(daily_fee))
    FROM car_rental_company_car
    WHERE car_type = 'SUV'
    GROUP BY car_type;