SELECT
	product_order_id,
	amount,
	price,
	total_sum,
	order_id,
	product_id,
	merchant_id,
	customer_id
FROM {{ source('order_source', 'product_order') }}
