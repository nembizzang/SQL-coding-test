SELECT cart_id
    FROM cart_products
    GROUP BY cart_id
    HAVING GROUP_CONCAT(name) LIKE '%Milk%'
           AND GROUP_CONCAT(name) LIKE '%Yogurt%' 
    ORDER BY cart_id;