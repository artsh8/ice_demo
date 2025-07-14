{{ config(materialized='table') }}

SELECT
    l.customer_id,
    c.first_name,
	c.last_name,
    c.email,
    l.merchant_id,
    m.name AS merchant_name,
    l.fav_merchant_by_products,
    l.fav_merchant_by_sum,
    l.fav_merchant_by_orders,
    l.combined_ranks
FROM {{ ref('customer_loyalty') }} l
JOIN {{ ref('merchant_base') }} m ON m.id = l.merchant_id
JOIN {{ ref('customer_base') }} c ON c.id = l.customer_id
