# 레코드 : total_sales = s.sales*b.price, a.author_id, a.author_name, b.category, s.sales
# 조건 : s.sales_date LIKE '2022-01%'
SELECT a.author_id, a.author_name, b.category, SUM(b.sales*b.price)
    FROM author a
    JOIN (SELECT b.book_id, b.category, b.author_id, b.price, s.sales
            FROM book b
            JOIN book_sales s
              ON b.book_id = s.book_id
            WHERE s.sales_date LIKE '2022-01%') b
      ON a.author_id = b.author_id
    GROUP BY a.author_id, b.category
    ORDER BY a.author_id, b.category DESC;
















# # join key : book.author_id = author.author_id / book.book_id = book_sales.book_id
# # 조건 : DATE_FORMAT(book_sales.sales_date,'%Y-%m') = '202201'
# SELECT author.author_id, author.author_name, b_s.category, SUM(b_s.price*b_s.sales)
#     FROM author
#     INNER JOIN (SELECT book.author_id, book.category, book.price, sales.sales
#                     FROM book
#                     INNER JOIN book_sales sales
#                             ON book.book_id = sales.book_id
#                     WHERE sales.sales_date LIKE '2022-01%') b_s
#             ON author.author_id = b_s.author_id
#     GROUP BY author.author_id, b_s.category
#     ORDER BY author.author_id, b_s.category DESC;