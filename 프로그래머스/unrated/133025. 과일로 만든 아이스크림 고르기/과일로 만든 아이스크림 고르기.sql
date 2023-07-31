SELECT f.FLAVOR
FROM first_half f, icecream_info i
WHERE f.flavor = i.flavor AND f.total_order >= 3000 AND i.ingredient_type = 'fruit_based'
ORDER BY total_order DESC