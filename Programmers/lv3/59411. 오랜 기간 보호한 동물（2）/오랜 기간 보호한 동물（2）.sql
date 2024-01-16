SELECT i.animal_id, i.name
    FROM animal_ins i
    LEFT OUTER JOIN animal_outs o
                ON i.animal_id = o.animal_id
    WHERE o.datetime IS NOT NULL
    ORDER BY o.datetime - i.datetime DESC
    LIMIT 2;



















# SELECT ins.animal_id, ins.name
#     FROM animal_ins ins
#     LEFT OUTER JOIN animal_outs outs
#                 ON ins.animal_id = outs.animal_id
#     ORDER BY outs.datetime - ins.datetime DESC
#     LIMIT 2;