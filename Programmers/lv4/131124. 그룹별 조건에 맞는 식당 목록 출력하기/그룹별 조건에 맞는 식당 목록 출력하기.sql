# 1. 리뷰 개수가 1등인 회원 id 추출
SELECT member_id
    FROM(SELECT member_id, RANK() OVER(ORDER BY COUNT(member_id) DESC) ranking
            FROM rest_review
            GROUP BY member_id) r
    WHERE ranking = 1;        
# 2. 해당 회원의 리뷰 추출
SELECT p.member_name name, r.review_text text, DATE_FORMAT(r.review_date, '%Y-%m-%d') date
    FROM MEMBER_PROFILE p
    JOIN rest_review r
      ON p.member_id = r.member_id
    WHERE p.member_id IN (SELECT member_id
                            FROM(SELECT member_id, RANK() OVER(ORDER BY COUNT(member_id) DESC) ranking
                                    FROM rest_review
                                    GROUP BY member_id) r
                            WHERE ranking = 1)
    ORDER BY date, text;














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