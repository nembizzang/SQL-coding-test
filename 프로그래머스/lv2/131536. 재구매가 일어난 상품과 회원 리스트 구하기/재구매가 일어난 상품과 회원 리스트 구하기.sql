SELECT user_id, product_id
FROM online_sale
GROUP BY product_id, user_id
HAVING COUNT(*)>= 2
ORDER BY user_id, product_id DESC