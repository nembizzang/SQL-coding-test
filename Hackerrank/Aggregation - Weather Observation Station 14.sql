# 문제 : https://www.hackerrank.com/challenges/weather-observation-station-14

SELECT ROUND(MAX(lat_n),4)
    FROM station
    WHERE lat_n < 137.2345;