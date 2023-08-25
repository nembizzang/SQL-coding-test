# 문제 : https://www.hackerrank.com/challenges/asian-population

SELECT SUM(city.population)
    FROM city
    INNER JOIN country
            ON city.countrycode = country.code
    WHERE country.continent = 'ASIA';