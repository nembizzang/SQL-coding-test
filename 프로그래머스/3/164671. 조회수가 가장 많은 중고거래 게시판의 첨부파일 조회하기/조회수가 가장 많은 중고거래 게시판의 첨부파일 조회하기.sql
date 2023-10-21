SELECT CONCAT('/home/grep/src/',f.board_id,'/',f.file_id,f.file_name,f.file_ext)
    FROM used_goods_board b
    JOIN used_goods_file f
      ON b.board_id = f.board_id
    WHERE b.board_id = (SELECT board_id
                         FROM USED_GOODS_BOARD
                         ORDER BY views DESC
                         LIMIT 1)
    ORDER BY file_id DESC;



















# SELECT CONCAT('/home/grep/src/',board.board_id,'/',file.file_id,file.file_name,file.file_ext) FILE_PATH
#     FROM used_goods_board board
#     INNER JOIN used_goods_file file
#             ON board.board_id = file.board_id
#     WHERE board.views = (SELECT MAX(views)
#                             FROM used_goods_board)
#     ORDER BY file.file_id DESC;