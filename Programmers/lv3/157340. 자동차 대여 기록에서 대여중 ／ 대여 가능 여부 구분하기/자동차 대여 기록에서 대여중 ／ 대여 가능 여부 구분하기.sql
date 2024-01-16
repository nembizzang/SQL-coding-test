SELECT a.car_id, IF(SUM(a.availability)=0, '대여 가능', '대여중') availability
    FROM (SELECT car_id, IF('2022-10-16' BETWEEN start_date AND end_date, 1, 0) availability
          FROM car_rental_company_rental_history) a
    GROUP BY a.car_id
    ORDER BY a.car_id DESC;















# SELECT DISTINCT(car_id) CAR_ID
#        , IF(car_id IN (SELECT car_id
#                          FROM car_rental_company_rental_history
#                         WHERE '2022-10-16' BETWEEN start_date and end_date),
#             '대여중','대여 가능') AVAILABILITY
#     FROM car_rental_company_rental_history
#     ORDER BY CAR_ID DESC;