# 문제 : https://www.hackerrank.com/challenges/weather-observation-station-19

SELECT ROUND(POW(POW(MAX(lat_n)-MIN(lat_n),2) + POW(MAX(long_w)-MIN(long_w),2),0.5),4)
    FROM station;