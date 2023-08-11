SELECT CONCAT('/home/grep/src/',board.board_id,'/',file.file_id,file.file_name,file.file_ext) FILE_PATH
    FROM used_goods_board board
    INNER JOIN used_goods_file file
            ON board.board_id = file.board_id
    WHERE board.views = (SELECT MAX(views)
                            FROM used_goods_board)
    ORDER BY file.file_id DESC;