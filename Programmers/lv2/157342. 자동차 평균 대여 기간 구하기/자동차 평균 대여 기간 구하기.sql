SELECT car_id, ROUND(AVG(DATEDIFF(end_date,start_date)+1),1) AVERAGE_DURATION
    FROM car_rental_company_rental_history
    GROUP BY car_id
    HAVING AVG(DATEDIFF(end_date,start_date)+1) >= 7.0
    ORDER BY AVERAGE_DURATION DESC, car_id DESC;