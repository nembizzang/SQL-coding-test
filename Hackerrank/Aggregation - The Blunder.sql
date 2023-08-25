# 문제 : https://www.hackerrank.com/challenges/the-blunder

SELECT ROUND(AVG(salary))-ROUND(AVG(replace(salary,'0','')))
    FROM employees;