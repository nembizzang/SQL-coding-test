# 1. 2021년에 가입한 전체 회원
SELECT user_id
    FROM user_info
    WHERE YEAR(joined) = '2021';

# 2. 2021년에 가입한 전체 회원 수
SELECT COUNT(user_id) FROM user_info WHERE YEAR(joined) = '2021';

# 3. sales 년 월 별로 구분
SELECT YEAR(sales_date) year, MONTH(sales_date) month, COUNT(DISTINCT(user_id)),
        ROUND(COUNT(DISTINCT(user_id))/(SELECT COUNT(user_id) FROM user_info WHERE YEAR(joined) = '2021'),1)
    FROM ONLINE_SALE
    WHERE user_id IN (SELECT user_id
                        FROM user_info
                        WHERE YEAR(joined) = '2021')
    GROUP BY year, month
    ORDER BY year, month;












# SELECT YEAR(sale.sales_date) year
#         , MONTH(sale.sales_date) month
#         , COUNT(DISTINCT sale.user_id) purchased_users
#         , ROUND(COUNT(DISTINCT sale.user_id)/(SELECT COUNT(*)
#                                                 FROM user_info
#                                                 WHERE YEAR(joined) = '2021'),1) purchased_ratio
#     FROM user_info info
#     INNER JOIN online_sale sale
#             ON info.user_id = sale.user_id
#     WHERE YEAR(info.joined) = '2021'
#     GROUP BY year, month
#     ORDER BY year, month;