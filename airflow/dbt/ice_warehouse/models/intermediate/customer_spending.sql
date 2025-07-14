WITH merchat_customer_order_agg AS (
SELECT
    merchant_id,
    customer_id,
    order_id,
    COUNT(*) AS num_products,
    SUM(total_sum) AS customer_sum_by_order
FROM {{ ref('product_order_base') }}
GROUP BY 
    merchant_id, 
    customer_id, 
    order_id
)

SELECT
    merchant_id,
    customer_id,
    order_id,
    num_products,
    SUM(num_products) OVER (PARTITION BY merchant_id, customer_id) AS cusomer_products_by_merchant,
    SUM(num_products) OVER (PARTITION BY customer_id) AS customer_total_products,
    customer_sum_by_order,
    SUM(customer_sum_by_order) OVER (PARTITION BY merchant_id, customer_id) AS customer_sum_by_merchant,
    SUM(customer_sum_by_order) OVER (PARTITION BY customer_id) AS customer_total_sum
FROM merchat_customer_order_agg
