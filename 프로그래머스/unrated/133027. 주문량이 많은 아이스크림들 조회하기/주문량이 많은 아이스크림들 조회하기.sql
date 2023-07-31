SELECT f.flavor
FROM first_half f, july j
WHERE f.flavor = j.flavor
GROUP BY f.flavor
ORDER BY (SUM(f.total_order) + SUM(j.total_order)) DESC
LIMIT 3