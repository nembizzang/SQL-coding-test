SELECT YEAR(sale.sales_date) year
        , MONTH(sale.sales_date) month
        , COUNT(DISTINCT sale.user_id) purchased_users
        , ROUND(COUNT(DISTINCT sale.user_id)/(SELECT COUNT(*)
                                                FROM user_info
                                                WHERE YEAR(joined) = '2021'),1) purchased_ratio
    FROM user_info info
    INNER JOIN online_sale sale
            ON info.user_id = sale.user_id
    WHERE YEAR(info.joined) = '2021'
    GROUP BY year, month
    ORDER BY year, month;