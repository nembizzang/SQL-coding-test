SELECT p.product_id, p.product_name, SUM(p.price*o.amount) total_price
    FROM food_product p
    LEFT OUTER JOIN food_order o 
                ON p.product_id = o.product_id
    WHERE o.produce_date LIKE '2022-05%'
    GROUP BY p.product_id, p.product_name
    ORDER BY total_price DESC, p.product_id;


















# SELECT prod.product_id, prod.product_name, SUM(prod.price*ord.amount) total_sales
#     FROM food_product prod
#     LEFT OUTER JOIN food_order ord
#                 ON prod.product_id = ord.product_id
#     WHERE DATE_FORMAT(ord.produce_date, '%Y%m') = '202205'
#     GROUP BY prod.product_id
#     ORDER BY total_sales DESC, prod.product_id;