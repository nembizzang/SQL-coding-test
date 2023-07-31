SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, ROUND(AVG(review_score),2) avg
FROM rest_info i, rest_review r
WHERE i.rest_id = r.rest_id AND LEFT(i.address,2) = '서울'
GROUP BY r.rest_id
ORDER BY avg DESC, i.favorites DESC