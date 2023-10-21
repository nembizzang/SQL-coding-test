SELECT i.rest_id, i.rest_name, i.food_type, i.favorites favs, i.address, ROUND(AVG(r.review_score),2) avgs
    FROM rest_info i
    JOIN rest_review r
      ON i.rest_id = r.rest_id
    WHERE i.address LIKE '서울%'
    GROUP BY r.rest_id
    ORDER BY avgs DESC, favs DESC;

# SELECT info.rest_id, info.rest_name, info.food_type, info.favorites, info.address,
#         ROUND(AVG(review.review_score),2) score
#     FROM rest_info info
#     INNER JOIN rest_review review
#             ON info.rest_id = review.rest_id
#     WHERE info.address LIKE '서울%'
#     GROUP BY rest_id
#     ORDER BY score DESC, info.favorites DESC;