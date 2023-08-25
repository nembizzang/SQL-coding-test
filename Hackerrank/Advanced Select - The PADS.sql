# 문제 : https://www.hackerrank.com/challenges/the-pads

SELECT CONCAT(name,'(',LEFT(occupation,1),')')
    FROM occupations
    ORDER BY name;
SELECT CONCAT('There are a total of ' , a.cnt, ' ', LOWER(a.occupation), IF(cnt>=2,'s.','.'))
    FROM (SELECT occupation, COUNT(*) cnt
            FROM occupations
            GROUP BY occupation) a
    GROUP BY occupation
    ORDER BY a.cnt, a.occupation;