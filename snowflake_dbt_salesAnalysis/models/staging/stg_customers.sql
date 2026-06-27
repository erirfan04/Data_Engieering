SELECT
customer_id,
customer_name,
city
FROM {{ ref('customers') }}