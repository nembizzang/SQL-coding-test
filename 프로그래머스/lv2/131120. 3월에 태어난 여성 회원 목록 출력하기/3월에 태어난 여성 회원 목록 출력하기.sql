SELECT member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d')
FROM member_profile
WHERE SUBSTRING(date_of_birth,6,2) = '03' AND gender = 'W' AND tlno IS NOT NULL
ORDER BY member_id