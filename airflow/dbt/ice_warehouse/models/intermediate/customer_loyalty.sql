WITH purchased AS (
SELECT
    customer_id,
    merchant_id,
    cusomer_products_by_merchant,
    customer_total_products,
    COUNT(*) AS num_orders,
    customer_sum_by_merchant,
    customer_total_sum
FROM {{ ref('customer_spending') }}
GROUP BY
    customer_id,
    merchant_id,
    cusomer_products_by_merchant,
    customer_total_products,
    customer_sum_by_merchant,
    customer_total_sum
),

ranking AS (
SELECT 
    *,
    DENSE_RANK() OVER (
        PARTITION BY customer_id
        ORDER BY cusomer_products_by_merchant DESC
    ) AS fav_merchant_by_products,
    DENSE_RANK() OVER (
        PARTITION BY customer_id
        ORDER BY customer_sum_by_merchant DESC
    ) AS fav_merchant_by_sum,
    DENSE_RANK() OVER (
        PARTITION BY customer_id
        ORDER BY num_orders DESC
    ) AS fav_merchant_by_orders
FROM purchased
)

SELECT
    *,
    (
        fav_merchant_by_products + fav_merchant_by_sum + fav_merchant_by_orders
    ) AS combined_ranks
FROM ranking
