SELECT product.product_code 상품코드, SUM(product.price*sale.sales_amount) 매출액
    FROM product product
    LEFT OUTER JOIN offline_sale sale
                ON product.product_id = sale.product_id
    WHERE sale.sales_amount IS NOT NULL
    GROUP BY product.product_code
    ORDER BY 매출액 DESC, 상품코드;