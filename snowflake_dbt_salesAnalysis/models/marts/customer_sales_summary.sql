SELECT
c.customer_name,
COUNT(o.order_id) AS total_orders,
SUM(o.amount) AS total_sales
FROM {{ ref('stg_customers') }} c
JOIN {{ ref('stg_orders') }} o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name