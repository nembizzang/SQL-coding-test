SELECT book.category, SUM(sales.sales)
    FROM book
    LEFT OUTER JOIN book_sales sales
                ON book.book_id = sales.book_id
    WHERE DATE_FORMAT(sales.sales_date, '%Y%m') = '202201'
    GROUP BY book.category
    ORDER BY book.category