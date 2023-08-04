SELECT fst.flavor
    FROM first_half fst
    LEFT OUTER JOIN icecream_info info
                ON fst.flavor = info.flavor
    WHERE fst.total_order > 3000 AND info.ingredient_type = 'fruit_based'
    ORDER BY fst.total_order DESC;