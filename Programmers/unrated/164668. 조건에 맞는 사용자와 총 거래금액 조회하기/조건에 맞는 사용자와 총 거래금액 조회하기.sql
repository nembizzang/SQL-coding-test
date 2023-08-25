SELECT board.writer_id USER_ID, user.nickname NICKNAME, sum(price) TOTAL_SALES
    FROM used_goods_board board
    LEFT OUTER JOIN used_goods_user user
                ON board.writer_id = user.user_id
    WHERE board.status = 'DONE'
    GROUP BY board.writer_id
    HAVING TOTAL_SALES >= 700000
    ORDER BY TOTAL_SALES;