SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth,'%Y-%m-%d')
    FROM member_profile
    WHERE MONTH(date_of_birth) = '03' and gender='W' and tlno IS NOT NULL
    ORDER BY member_id
    