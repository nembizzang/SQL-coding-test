SELECT f.flavor
    FROM first_half f
    JOIN july j
      ON f.flavor = j.flavor
    GROUP BY f.flavor
    ORDER BY SUM(f.total_order)+SUM(j.total_order) DESC
    LIMIT 3;



















# SELECT f.flavor
#     FROM first_half f
#     INNER JOIN july j
#             ON f.flavor = j.flavor
#     GROUP BY f.flavor
#     ORDER BY SUM(f.total_order+j.total_order) DESC
#     LIMIT 3;