# 문제 : https://www.hackerrank.com/challenges/weather-observation-station-9

SELECT DISTINCT(city)
    FROM station
    WHERE LEFT(city,1) NOT IN ('a','e','i','o','u')