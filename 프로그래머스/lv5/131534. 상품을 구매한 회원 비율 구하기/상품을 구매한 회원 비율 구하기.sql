# 2021년에 가입하고 상품을 구매한 회원리스트
# SELECT COUNT(DISTINCT u.user_id)
# FROM user_info u
# JOIN online_sale o
# ON o.user_id = u.user_id
# WHERE u.user_id IN (SELECT user_id FROM user_info WHERE YEAR(joined)='2021')


SELECT YEAR(sales_date) YEAR, MONTH(sales_date) MONTH, COUNT(DISTINCT u.user_id) PUCHASED_USERS,
        ROUND(COUNT(DISTINCT u.user_id)/(SELECT COUNT(DISTINCT user_id)
                                        FROM user_info
                                        WHERE user_id IN (SELECT user_id FROM user_info WHERE YEAR(joined)='2021')),1) PUCHASED_RATIO
FROM user_info u
JOIN online_sale o
ON u.user_id = o.user_id
WHERE u.user_id IN (SELECT user_id FROM user_info WHERE YEAR(joined)='2021')
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH