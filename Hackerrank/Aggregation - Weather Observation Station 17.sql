# 문제 : https://www.hackerrank.com/challenges/weather-observation-station-17

SELECT ROUND(long_w,4)
    FROM station
    WHERE lat_n = (SELECT MIN(lat_n)
                    FROM station
                    WHERE lat_n > 38.7780);