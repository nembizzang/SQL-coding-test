SELECT prod.product_id, prod.product_name, SUM(prod.price*ord.amount) total_sales
    FROM food_product prod
    LEFT OUTER JOIN food_order ord
                ON prod.product_id = ord.product_id
    WHERE DATE_FORMAT(ord.produce_date, '%Y%m') = '202205'
    GROUP BY prod.product_id
    ORDER BY total_sales DESC, prod.product_id;