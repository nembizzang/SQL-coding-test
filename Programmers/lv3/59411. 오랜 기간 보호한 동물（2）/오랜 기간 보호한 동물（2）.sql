SELECT ins.animal_id, ins.name
    FROM animal_ins ins
    LEFT OUTER JOIN animal_outs outs
                ON ins.animal_id = outs.animal_id
    ORDER BY outs.datetime - ins.datetime DESC
    LIMIT 2;