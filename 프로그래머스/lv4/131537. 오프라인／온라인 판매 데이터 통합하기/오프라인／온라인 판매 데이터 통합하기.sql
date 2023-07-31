SELECT DATE_FORMAT(sales_date,'%Y-%m-%d') SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM 
(SELECT SALES_DATE, PRODUCT_ID, NULL USER_ID, SUM(sales_amount) SALES_AMOUNT
FROM offline_sale
GROUP BY sales_date, product_id
UNION
SELECT SALES_DATE, PRODUCT_ID, USER_ID, SUM(sales_amount) SALES_AMOUNT
FROM online_sale
GROUP BY sales_date, product_id, user_id) m
WHERE DATE_FORMAT(SALES_DATE,'%y%m') = '2203'
ORDER BY sales_date, product_id, user_id