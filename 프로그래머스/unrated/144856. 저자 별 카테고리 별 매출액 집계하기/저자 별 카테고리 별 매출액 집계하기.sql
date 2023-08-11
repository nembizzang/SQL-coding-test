# join key : book.author_id = author.author_id / book.book_id = book_sales.book_id
# 조건 : DATE_FORMAT(book_sales.sales_date,'%Y-%m') = '202201'
SELECT author.author_id, author.author_name, b_s.category, b_s.total_sales
    FROM author
    INNER JOIN (SELECT book.author_id, book.category, SUM(book.price*sales.sales) total_sales
                    FROM book
                    INNER JOIN book_sales sales
                            ON book.book_id = sales.book_id
                    WHERE sales.sales_date LIKE '2022-01%'
                    GROUP BY book.author_id, book.category) b_s
            ON author.author_id = b_s.author_id
    ORDER BY author.author_id, b_s.category DESC;
    