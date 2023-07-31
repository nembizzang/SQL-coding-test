WITH RECURSIVE tmp AS (
SELECT 0 hour
UNION ALL
SELECT hour+1 FROM tmp WHERE hour < 23)

SELECT t.hour HOUR, IFNULL(h.count,0) COUNT
FROM tmp t
LEFT JOIN (SELECT HOUR(datetime) hour, COUNT(animal_id) count
FROM animal_outs
GROUP BY hour) h
ON t.hour = h.hour
GROUP BY HOUR
ORDER BY HOUR