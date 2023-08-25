# 문제 : https://www.hackerrank.com/challenges/what-type-of-triangle

SELECT
    (CASE WHEN a>=b+c OR b>=c+a OR c>=a+b THEN 'Not A Triangle'
          WHEN a=b AND b=c THEN 'Equilateral'
          WHEN (a=b AND b!=c) OR (b=c AND c!=a) OR (c=a AND a!=b) THEN 'Isosceles'
          ELSE 'Scalene'
      END)
    FROM triangles;