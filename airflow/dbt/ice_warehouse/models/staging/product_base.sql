SELECT
	id,
	merchant_id,
	price,
	amount,
	name
FROM {{ source('order_source', 'product') }}
