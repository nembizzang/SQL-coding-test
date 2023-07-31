SELECT m.member_name MEMBER_NAME, r.review_text REVIEW_TEXT, DATE_FORMAT(r.review_date, '%Y-%m-%d') REVIEW_DATE
FROM member_profile m
JOIN rest_review r
ON m.member_id = r.member_id
WHERE r.member_id in (SELECT member_id
                    FROM rest_review
                   GROUP BY member_id
                     HAVING COUNT(*) = (SELECT MAX(a.cnt)
                                        FROM(SELECT member_id, COUNT(member_id) cnt
                                        FROM rest_review
                                        GROUP BY member_id) a))
ORDER BY REVIEW_DATE, REVIEW_TEXT

# SELECT PRO.MEMBER_NAME, REV.REVIEW_TEXT, DATE_FORMAT(REV.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE FROM MEMBER_PROFILE PRO
# JOIN REST_REVIEW REV 
# ON REV.MEMBER_ID = PRO.MEMBER_ID
# WHERE PRO.MEMBER_NAME = (SELECT PROF.MEMBER_NAME FROM MEMBER_PROFILE PROF
#                          JOIN REST_REVIEW REST
#                          ON REST.MEMBER_ID = PROF.MEMBER_ID
#                          GROUP BY MEMBER_NAME
#                          ORDER BY COUNT(MEMBER_NAME) DESC
#                          LIMIT 1)
# ORDER BY REV.REVIEW_DATE, REV.REVIEW_TEXT