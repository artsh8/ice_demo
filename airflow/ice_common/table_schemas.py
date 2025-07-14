customer = """\
CREATE TABLE IF NOT EXISTS iceberg.order_source.customer (
    id bigint NOT NULL,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    email varchar
)
WITH (
    format = 'PARQUET'
)
"""
merchant = """\
CREATE TABLE IF NOT EXISTS iceberg.order_source.merchant (
    id bigint NOT NULL,
    name varchar NOT NULL
)
WITH (
    format = 'PARQUET'
)    
"""
product = """\
CREATE TABLE IF NOT EXISTS iceberg.order_source.product (
    id bigint NOT NULL,
    merchant_id bigint NOT NULL,
    price bigint NOT NULL,
    amount integer NOT NULL,
    name varchar NOT NULL
    )
WITH (
    format = 'PARQUET'
)
"""
product_order = """\
CREATE TABLE IF NOT EXISTS iceberg.order_source.product_order (
    product_order_id bigint NOT NULL,
    amount integer NOT NULL,
    price bigint NOT NULL,
    total_sum bigint NOT NULL,
    order_id bigint NOT NULL,
    product_id bigint NOT NULL,
    merchant_id bigint NOT NULL,
    customer_id bigint NOT NULL
)
WITH (
    format = 'PARQUET'
)
"""
