SELECT 
	id,
	name
FROM {{ source('order_source', 'merchant') }}
