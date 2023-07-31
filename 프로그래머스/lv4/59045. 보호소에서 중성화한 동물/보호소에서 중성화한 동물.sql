SELECT a.animal_id, a.animal_type, a.name
FROM animal_ins a
JOIN animal_outs o
ON a.animal_id=o.animal_id AND a.animal_type=o.animal_type AND a.name=o.name
WHERE sex_upon_intake LIKE '%Intact%' AND sex_upon_outcome NOT LIKE '%Intact%'
ORDER BY animal_id