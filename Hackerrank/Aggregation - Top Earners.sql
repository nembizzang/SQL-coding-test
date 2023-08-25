# 문제 : https://www.hackerrank.com/challenges/earnings-of-employees

SELECT months*salary, COUNT(*)
    FROM employee
    WHERE months*salary = (SELECT max(months*salary)
                            FROM employee)
    GROUP BY months*salary;