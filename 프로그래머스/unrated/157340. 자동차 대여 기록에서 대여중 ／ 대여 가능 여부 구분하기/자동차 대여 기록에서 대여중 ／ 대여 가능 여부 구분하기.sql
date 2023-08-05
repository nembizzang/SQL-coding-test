SELECT history.car_id CAR_ID
       ,(CASE WHEN GROUP_CONCAT(DISTINCT(able.a)) LIKE '%대여중%' THEN '대여중'
              ELSE '대여 가능'
        END) AVAILABILITY
    FROM car_rental_company_rental_history history
    INNER JOIN (SELECT car_id, start_date, (CASE WHEN ('2022-10-16' >= start_date
                                   AND '2022-10-16' <= end_date) THEN '대여중'
                        ELSE '대여 가능'
                        END) a
                  FROM car_rental_company_rental_history) able
            ON history.car_id = able.car_id AND history.start_date = able.start_date
    GROUP BY history.car_id
    ORDER BY CAR_ID DESC;