SELECT DATE_FORMAT(a.sales_date, '%Y-%m-%d') date, a.product_id, a.user_id, a.sales_amount
    FROM
        ((SELECT sales_date, product_id, user_id, sales_amount
            FROM online_sale)
        UNION
        (SELECT sales_date, product_id, NULL user_id, sales_amount
            FROM offline_sale)) a
    WHERE MONTH(sales_date) = 3
    ORDER BY date, product_id, user_id;


















# SELECT DATE_FORMAT(sales_date,'%Y-%m-%d'), product_id, IFNULL(user_id,NULL) user_id, sales_amount
#     FROM (SELECT sales_date, product_id, user_id, sales_amount
#             FROM online_sale
#           UNION
#           SELECT sales_date, product_id, NULL, sales_amount
#             FROM offline_sale) a
#     WHERE sales_date LIKE '2022-03%'
#     ORDER BY sales_date, product_id, user_id;