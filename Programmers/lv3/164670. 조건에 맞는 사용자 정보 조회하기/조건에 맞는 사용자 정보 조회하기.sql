SELECT DISTINCT(b.writer_id), u.nickname, CONCAT_WS(' ',u.city,u.street_address1,u.street_address2),
        CONCAT_WS('-',LEFT(u.tlno,3),SUBSTRING(u.tlno,4,4),RIGHT(u.tlno,4))
    FROM used_goods_board b
    LEFT OUTER JOIN used_goods_user u
                ON b.writer_id = u.user_id
    WHERE b.writer_id IN (SELECT writer_id
                            FROM used_goods_board
                            GROUP BY writer_id
                            HAVING COUNT(writer_id) >= 3)
    ORDER BY b.writer_id DESC;





















# SELECT users.user_id USER_ID
#     , users.nickname NICKNAME
#     , CONCAT_WS(' ', users.CITY, users.street_address1, users.street_address2) 전체주소
#     , CONCAT_WS('-', LEFT(users.tlno,3), SUBSTRING(users.tlno,4,4), RIGHT(users.tlno,4)) 전화번호
#     FROM used_goods_board boards
#     INNER JOIN used_goods_user users
#             ON boards.writer_id = users.user_id
#     GROUP BY USER_ID
#     HAVING COUNT(USER_ID) >= 3
#     ORDER BY USER_ID DESC;