SELECT
    product_id,
    product_name,
    merchant_name,
    product_stock,
    num_product_ordered,
    product_stock - num_product_ordered AS remaining_stock
FROM {{ ref('product_popularity') }}
