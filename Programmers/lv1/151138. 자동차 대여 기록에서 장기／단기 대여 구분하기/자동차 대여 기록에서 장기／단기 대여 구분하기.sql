SELECT history_id, car_id,
       DATE_FORMAT(start_date,'%Y-%m-%d'), DATE_FORMAT(end_date,'%Y-%m-%d'),
       IF(DATEDIFF(end_date,start_date)+1>=30,'장기 대여', '단기 대여') RENT_TYPE
    FROM car_rental_company_rental_history
    WHERE start_date LIKE '2022-09%'
    ORDER BY history_id DESC;