SELECT sales_date, product_id, IFNULL(user_id,NULL) user_id, sales_amount
    FROM (SELECT DATE_FORMAT(sales_date,'%Y-%m-%d') sales_date, product_id, user_id, sales_amount
            FROM online_sale
          UNION
          SELECT sales_date, product_id, NULL, sales_amount
            FROM offline_sale) a
    WHERE sales_date LIKE '2022-03%'
    ORDER BY sales_date, product_id, user_id;