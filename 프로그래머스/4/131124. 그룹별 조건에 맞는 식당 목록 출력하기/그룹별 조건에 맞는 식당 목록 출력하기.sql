SELECT p.member_name, r.review_text, DATE_FORMAT(r.review_date,'%Y-%m-%d')
    FROM member_profile p
    JOIN rest_review r
      ON p.member_id = r.member_id
    WHERE p.member_id IN (SELECT member_id
                            FROM rest_review
                            GROUP BY member_id
                            HAVING COUNT(member_id) = (SELECT max(cnt)
                                                            FROM (SELECT COUNT(member_id) cnt
                                                                    FROM rest_review
                                                                    GROUP BY member_id) a)
                                )
    ORDER BY review_date, review_text;
    








# SELECT p.member_name, r.review_text, DATE_FORMAT(r.review_date,'%Y-%m-%d')
#     FROM member_profile p
#     INNER JOIN rest_review r
#             ON p.member_id = r.member_id
#     WHERE p.member_id IN (SELECT member_id
#                             FROM rest_review
#                             GROUP BY member_id
#                             HAVING COUNT(member_id) = (SELECT MAX(cnt)
#                                                          FROM (SELECT COUNT(member_id) cnt
#                                                                  FROM rest_review
#                                                                  GROUP BY member_id) a))
#     ORDER BY review_date, review_text;