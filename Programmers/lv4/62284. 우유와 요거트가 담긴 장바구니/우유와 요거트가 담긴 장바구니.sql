SELECT y.cart_id
    FROM (SELECT DISTINCT cart_id
            FROM cart_products
            WHERE name = 'Yogurt') y
    JOIN (SELECT DISTINCT cart_id
            FROM cart_products
            WHERE name = 'Milk') m
      ON y.cart_id = m.cart_id
    ORDER BY y.cart_id;




















# # GROUP_CONCAT 활용
# SELECT cart_id
#     FROM cart_products
#     GROUP BY cart_id
#     HAVING GROUP_CONCAT(name) LIKE '%Milk%'
#            AND GROUP_CONCAT(name) LIKE '%Yogurt%' 
#     ORDER BY cart_id;

# # sub query 활용
# SELECT DISTINCT cart_id
# FROM cart_products
# WHERE name = 'Milk'
# AND cart_id in (SELECT cart_id FROM cart_products WHERE name = 'Yogurt')
# ORDER BY cart_id;

# # IN, DISTNICT 활용
# SELECT cart_id
# FROM cart_products
# WHERE name IN ('Milk', 'Yogurt')
# GROUP BY cart_id
# HAVING COUNT(DISTINCT name) >= 2
# ORDER BY cart_id;