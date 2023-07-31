SELECT i.ingredient_type, SUM(f.total_order) total_order
FROM first_half f, icecream_info i
WHERE f.flavor = i.flavor
GROUP BY i.ingredient_type
ORDER BY total_order