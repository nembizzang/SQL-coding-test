SELECT p.product_id, p.product_name, SUM(p.price*o.amount) TOTAL_SALES
FROM food_product p, food_order o
WHERE p.product_id = o.product_id AND DATE_FORMAT(o.produce_date,'%y%m') = '2205'
GROUP BY product_id
ORDER BY total_sales DESC, product_id