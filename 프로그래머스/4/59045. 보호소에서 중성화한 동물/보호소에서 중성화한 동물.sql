SELECT i.animal_id, i.animal_type, i.name
    FROM animal_ins i
    LEFT OUTER JOIN animal_outs o
                ON i.animal_id = o.animal_id
    WHERE  i.sex_upon_intake Like 'Intact%' AND o.sex_upon_outcome NOT LIKE 'Intact%'
    ORDER BY i.animal_id;
    




















# SELECT ins.animal_id, ins.animal_type, ins.name
#     FROM animal_ins ins
#     LEFT OUTER JOIN animal_outs outs
#                 ON ins.animal_id = outs.animal_id
#     WHERE (ins.sex_upon_intake LIKE '%Intact%')
#         AND (outs.sex_upon_outcome LIKE '%Spayed%' OR outs.sex_upon_outcome LIKE '%Neutered%')
#     ORDER BY ins.animal_id;