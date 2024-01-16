SELECT i.food_type, i.rest_id, i.rest_name, i.favorites
    FROM rest_info i 
    JOIN (SELECT food_type, MAX(favorites) f
            FROM rest_info
            GROUP BY food_type) b
        ON i.food_type = b.food_type AND i.favorites = b.f
    ORDER BY i.food_type DESC;
                    

















# # Subquery - inner view 활용
# SELECT info.food_type, info.rest_id, info.rest_name, info.favorites
#     FROM rest_info info
#     INNER JOIN (SELECT food_type, MAX(favorites) favorites
#                             FROM rest_info
#                             GROUP BY food_type) fav
#                 ON info.favorites = fav.favorites AND info.food_type=fav.food_type
#     ORDER BY info.food_type DESC;
    
# # Subquery - scalar 활용
# SELECT food_type, rest_id, rest_name, favorites
# FROM rest_info
# WHERE favorites IN (SELECT MAX(favorites) FROM rest_info GROUP BY food_type)
# GROUP BY food_type
# ORDER BY food_type DESC