SELECT category, price MAX_PRICE, product_name
FROM food_product
WHERE category IN ('과자', '국', '김치', '식용유')
AND price IN (SELECT MAX(PRICE) FROM food_product GROUP BY category)
ORDER BY price DESC

# SELECT category, MAX(PRICE), product_name
# FROM food_product
# GROUP BY category
# HAVING category IN ('과자', '국', '김치', '식용유')
# ORDER BY price DESC