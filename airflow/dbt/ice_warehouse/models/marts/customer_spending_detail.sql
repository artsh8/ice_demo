{{ config(materialized='table') }}

SELECT
    s.merchant_id,
    m.name AS merchant_name,
    s.customer_id,
    c.first_name,
	c.last_name,
    c.email,
    s.order_id,
    num_products,
    s.cusomer_products_by_merchant,
    s.customer_total_products,
    {{ to_money('s.customer_sum_by_order') }} AS customer_sum_by_order,
    {{ to_money('s.customer_sum_by_merchant') }} AS customer_sum_by_merchant,
    {{ to_money('s.customer_total_sum') }} AS customer_total_sum
FROM {{ ref('customer_spending') }} s
JOIN {{ ref('merchant_base') }} m ON m.id = s.merchant_id
JOIN {{ ref('customer_base') }} c ON c.id = s.customer_id
