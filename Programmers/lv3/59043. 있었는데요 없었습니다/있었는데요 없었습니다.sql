SELECT i.animal_id, i.name
    FROM animal_ins i
    LEFT OUTER JOIN animal_outs o
                ON i.animal_id = o.animal_id
    WHERE i.datetime > o.datetime
    ORDER BY i.datetime ;


















# SELECT ins.animal_id, ins.name
#     FROM animal_ins ins
#     LEFT OUTER JOIN animal_outs outs
#                 ON ins.animal_id = outs.animal_id
#     WHERE ins.datetime > outs.datetime
#     ORDER BY ins.datetime;