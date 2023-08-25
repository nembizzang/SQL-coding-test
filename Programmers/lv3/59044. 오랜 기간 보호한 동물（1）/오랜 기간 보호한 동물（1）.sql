SELECT ins.name, ins.datetime
    FROM animal_ins ins
    LEFT OUTER JOIN animal_outs outs
                ON ins.animal_id = outs.animal_id
    WHERE outs.datetime IS NULL
    ORDER BY ins.datetime
    LIMIT 3;