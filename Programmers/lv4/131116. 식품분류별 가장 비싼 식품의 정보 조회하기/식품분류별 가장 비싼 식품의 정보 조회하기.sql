SELECT f.category, f.price, f.product_name
    FROM food_product f
    JOIN (SELECT category, MAX(price) price
            FROM food_product
            GROUP BY category) p
        ON f.category = p.category and f.price = p.price
    WHERE f.category IN ('과자', '국', '김치', '식용유')
    ORDER BY f.price DESC;



















# SELECT food.category, food.price, food.product_name
#     FROM food_product food
#     INNER JOIN (SELECT category, MAX(price) price
#                     FROM food_product
#                     GROUP BY category) p
#             ON food.category = p.category AND food.price = p.price
#     WHERE food.category IN ('과자','국','김치','식용유')
#     ORDER BY food.price DESC;