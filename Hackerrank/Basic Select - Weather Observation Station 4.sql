# 문제 : https://www.hackerrank.com/challenges/weather-observation-station-4

SELECT COUNT(city)-COUNT(DISTINCT city)
    FROM station;