SELECT YEAR(s.sales_date) year, MONTH(s.sales_date) month, i.gender, COUNT(DISTINCT i.user_id)
    FROM user_info i
    JOIN online_sale s
      ON i.user_id = s.user_id
    WHERE gender IS NOT NULL
    GROUP BY YEAR(s.sales_date), MONTH(s.sales_date), i.gender
    ORDER BY year, month, gender ;

















# SELECT YEAR(sale.sales_date) YEAR
#         , MONTH(sale.sales_date) MONTH
#         , info.gender GENDER
#         , COUNT(DISTINCT(info.user_id)) USERS
#     FROM user_info info
#     INNER JOIN online_sale sale
#             ON info.user_id = sale.user_id
#     WHERE info.gender IS NOT NULL
#     GROUP BY YEAR, MONTH, GENDER
#     ORDER BY YEAR, MONTH, GENDER;