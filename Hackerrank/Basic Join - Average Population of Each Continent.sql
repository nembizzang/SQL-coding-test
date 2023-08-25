# 문제 : https://www.hackerrank.com/challenges/average-population-of-each-continent

SELECT country.continent, FLOOR(AVG(city.population))
    FROM city
    INNER JOIN country
            ON city.countrycode = country.code
    GROUP BY country.continent;