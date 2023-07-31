SELECT ins.animal_id, ins.animal_type, ins.name
    FROM animal_ins ins
    LEFT OUTER JOIN animal_outs outs
                ON ins.animal_id = outs.animal_id
    WHERE (ins.sex_upon_intake LIKE '%Intact%')
        AND (outs.sex_upon_outcome LIKE '%Spayed%' OR outs.sex_upon_outcome LIKE '%Neutered%')
    ORDER BY ins.animal_id;