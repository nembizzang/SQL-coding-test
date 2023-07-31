SELECT
    (CASE
        WHEN 10000 <= price AND price < 20000 THEN 10000
        WHEN 20000 <= price AND price < 30000 THEN 20000
        WHEN 30000 <= price AND price < 40000 THEN 30000
        WHEN 40000 <= price AND price < 50000 THEN 40000
        WHEN 50000 <= price AND price < 60000 THEN 50000
        WHEN 60000 <= price AND price < 70000 THEN 60000
        WHEN 70000 <= price AND price < 80000 THEN 70000
        ELSE 80000
     END) price_group,
     COUNT(*) products
FROM product
GROUP BY price_group
ORDER BY price_group