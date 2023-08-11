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
    
    
#     SELECT YEAR(sales_date),
#     MONTH(sales_date), 
#     count(DISTINCT O.USER_ID), 
#     ROUND(count(DISTINCT O.USER_ID)/(SELECT COUNT(USER_ID) FROM USER_INFO WHERE YEAR(JOINED) = 2021),1)
# FROM ONLINE_SALE O
# INNER JOIN USER_INFO U ON U.USER_ID = O.USER_ID
# WHERE YEAR(JOINED) = 2021
# GROUP BY 1,2
# ORDER BY 1,2