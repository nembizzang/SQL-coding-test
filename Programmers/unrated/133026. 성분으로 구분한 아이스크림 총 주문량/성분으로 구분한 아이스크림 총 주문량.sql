SELECT info.ingredient_type, SUM(fh.total_order) TOTAL_ORDER
    FROM first_half fh
    LEFT OUTER JOIN icecream_info info
                ON fh.flavor = info.flavor
    GROUP BY info.ingredient_type
    ORDER BY fh.total_order;