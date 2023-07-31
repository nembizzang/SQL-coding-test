SELECT ins.animal_id, ins.name
    FROM animal_ins ins
    LEFT OUTER JOIN animal_outs outs
                ON ins.animal_id = outs.animal_id
    WHERE ins.datetime > outs.datetime
    ORDER BY ins.datetime;