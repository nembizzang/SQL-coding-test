# 문제 : https://www.hackerrank.com/challenges/weather-observation-station-6

SELECT DISTINCT(city)
    FROM station
    WHERE LEFT(city,1) IN ('a','e','i','o','u');