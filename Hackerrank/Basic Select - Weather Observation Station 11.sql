# 문제 : https://www.hackerrank.com/challenges/weather-observation-station-11

SELECT DISTINCT(city)
    FROM station
    WHERE (LEFT(city,1) NOT IN ('a','e','i','o','u'))
                OR (RIGHT(city,1) NOT IN ('a','e','i','o','u'));