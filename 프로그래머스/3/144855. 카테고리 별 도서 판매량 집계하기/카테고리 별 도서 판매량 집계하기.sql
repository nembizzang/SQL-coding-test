# SELECT book.category, SUM(sales.sales)
#     FROM book
#     LEFT OUTER JOIN book_sales sales
#                 ON book.book_id = sales.book_id
#     WHERE DATE_FORMAT(sales.sales_date, '%Y%m') = '202201'
#     GROUP BY book.category
#     ORDER BY book.category
















SELECT b.category, SUM(s.sales) total_sales
    FROM book b
    JOIN book_sales s
        ON b.book_id = s.book_id
    WHERE s.sales_date LIKE '2022-01%'
    GROUP BY b.category
    ORDER BY b.category;