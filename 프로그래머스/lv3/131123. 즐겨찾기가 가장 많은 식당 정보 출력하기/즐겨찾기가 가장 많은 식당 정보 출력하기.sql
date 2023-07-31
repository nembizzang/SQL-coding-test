# SELECT food_type, rest_id, rest_name, favorites
# FROM rest_info
# WHERE favorites IN (SELECT MAX(favorites) FROM rest_info GROUP BY food_type)
# GROUP BY food_type
# ORDER BY food_type DESC

SELECT a.food_type, a.rest_id, a.rest_name, a.favorites
FROM rest_info a
JOIN (SELECT MAX(favorites) favorites, food_type FROM rest_info GROUP BY food_type) b
WHERE a.favorites = b.favorites AND a.food_type = b.food_type
ORDER BY food_type DESC