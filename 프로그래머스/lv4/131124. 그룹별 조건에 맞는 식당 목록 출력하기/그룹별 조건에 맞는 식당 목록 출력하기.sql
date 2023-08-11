SELECT p.member_name, r.review_text REVIEW_TEXT, DATE_FORMAT(r.review_date,'%Y-%m-%d') REVIEW_DATE
    FROM member_profile p
    INNER JOIN rest_review r
            ON p.member_id = r.member_id
    WHERE p.member_id IN (SELECT member_id
                            FROM rest_review
                            GROUP BY member_id
                            HAVING COUNT(member_id) = (SELECT MAX(cnt)
                                                         FROM (SELECT COUNT(member_id) cnt
                                                                 FROM rest_review
                                                                 GROUP BY member_id) a))
    ORDER BY REVIEW_DATE, REVIEW_TEXT;