SELECT LEFT(product_code,2) cd, COUNT(*)
    FROM product
    GROUP BY cd
    ORDER BY product_code;