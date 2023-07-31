SELECT DATE_FORMAT(o.sales_date, '%Y') YEAR, DATE_FORMAT(o.sales_date, '%c') MONTH, u.gender GENDER, COUNT(DISTINCT u.user_id) USERS
FROM user_info u, online_sale o
WHERE u.user_id = o.user_id AND u.gender IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, DATE_FORMAT(o.sales_date, '%m'), GENDER