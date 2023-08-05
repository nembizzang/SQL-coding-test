SELECT YEAR(sale.sales_date) YEAR
    , MONTH(sale.sales_date) MONTH
    , info.gender GENDER
    , COUNT(DISTINCT(info.user_id)) USERS
    FROM user_info info
    INNER JOIN online_sale sale
                 ON info.user_id = sale.user_id
    WHERE info.gender IS NOT NULL
    GROUP BY YEAR, MONTH, GENDER
    ORDER BY YEAR, MONTH, GENDER;