# 레코드 car_id, car_type, fee
# 조건 1: 세단, SUV
# 조건 2: 2022년 11월 1일 ~ 2022년 11월 30일 대여 가능
# 조건 3: 대여 금액 50만원 이상 200미만
# 할인율 : (7~29), (30~90), (90~)
# fee = 30*daily_fee*할인율
# 1. 대여 가능한 car_id, car_type 추출
# 2. car_id, car_type에 맞는 '30일 이상'의 discount_rate 찾기
# 3. fee 계산
SELECT c.car_id, c.car_type, ROUND(30*c.daily_fee*(100-p.discount_rate)/100) fee
    FROM CAR_RENTAL_COMPANY_CAR c
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
      ON c.car_type = p.car_type
    WHERE c.car_type IN ('세단','SUV') AND p.duration_type = '30일 이상'
        AND c.car_id IN (SELECT car_id
                            FROM (SELECT car_id, IF(start_date > '2022-11-30' OR end_date < '2022-11-01',0,1) avail
                                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) a
                            GROUP BY car_id
                            HAVING SUM(avail) = 0)
    HAVING fee >= 500000 AND fee < 2000000
    ORDER BY fee DESC, c.car_type, c.car_id DESC;



# # output : c.car_id, c.car_type, fee((DATEDIFF(h.end_date,h.start_date)+1)*c.daily_fee*d.discount_rate(대여일에 따라 d.duration_type에 맞는 d.discount_rate 입력)
# # 조건 : c.car_type IN ('세단','SUV'), h.end_date < '2022-11-01' OR h.start_date < '2022-11-30', fee BETWEEN(50,200)
# # alias : car_rental_company_car c, car_rental_company_rental_history h, car_rental_company_discount_plan d
# # JOIN KEY : c.car_id = h.car_id / c.car_type = d.car_type

# SELECT f.car_id, f.car_type, ROUND(30*f.daily_fee*(100-discount_rate)/100) fee
#     FROM  (SELECT car_id, car_type, daily_fee
#             FROM car_rental_company_car
#             WHERE car_id IN (SELECT car_id
#                                 FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#                                 GROUP BY car_id
#                                 HAVING COUNT(car_id) = SUM((CASE WHEN end_date < '2022-11-01' OR start_date > '2022-11-30' THEN 1
#                                                                  ELSE 0
#                                                             END))
#                              )
#            ) f
#     INNER JOIN car_rental_company_discount_plan d
#             ON f.car_type = d.car_type
#     WHERE d.duration_type = '30일 이상' AND f.car_type IN ('세단','SUV')
#     HAVING fee BETWEEN 500000 AND 2000000
#     ORDER BY fee DESC, car_type, car_id DESC;