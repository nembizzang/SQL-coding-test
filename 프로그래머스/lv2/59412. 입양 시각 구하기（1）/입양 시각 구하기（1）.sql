SELECT HOUR(datetime) HOUR, COUNT(*) COUNT
    FROM animal_outs
    GROUP BY HOUR
    HAVING HOUR between 9 and 19
    ORDER BY HOUR;