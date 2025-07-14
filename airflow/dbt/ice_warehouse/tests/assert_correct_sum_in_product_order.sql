SELECT amount
FROM {{ ref('product_order_base') }}
WHERE amount * price != total_sum
