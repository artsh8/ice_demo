WITH product_ordered AS (
SELECT
	product_id,
	SUM(amount) AS num_product_ordered
FROM {{ ref('product_order_base') }}
GROUP BY product_id
)

SELECT
	po.product_id,
	p.name AS product_name,
	p.amount AS product_stock,
	p.merchant_id,
	m.name AS merchant_name,
	po.num_product_ordered
FROM product_ordered po
JOIN {{ ref('product_base') }} p ON p.id = po.product_id
JOIN {{ ref('merchant_base') }} m ON m.id = p.merchant_id
