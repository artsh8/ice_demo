from ice_common import table_schemas

CONN_TRINO = "trino_default"
DBT_PROJECT_DIR = DBT_PROFILE_DIR = "/root/airflow/dbt/ice_warehouse"
DBT_MARTS_DIR = "models/marts"

order_source_schema_create = (
    "CREATE SCHEMA IF NOT EXISTS iceberg.order_source WITH (location = 's3a://source/')"
)
order_source_schema_drop = "DROP SCHEMA IF EXISTS iceberg.order_source"

all_tables_create = [
    value for name, value in vars(table_schemas).items() if not name.startswith("__")
]

customer_load_full = """\
MERGE INTO iceberg.order_source.customer t
USING (
    SELECT id, first_name, last_name, email
    FROM sourcedb.public.customer
) s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET
    first_name = s.first_name,
    last_name = s.last_name,
    email = s.email
WHEN NOT MATCHED THEN INSERT (id, first_name, last_name, email)
VALUES (s.id, s.first_name, s.last_name, s.email)
"""
customer_drop = "DROP TABLE IF EXISTS iceberg.order_source.customer"

merchant_load_full = """\
MERGE INTO iceberg.order_source.merchant t
USING (
    SELECT id, name
    FROM sourcedb.public.merchant
) s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET
    name = s.name
WHEN NOT MATCHED THEN INSERT (id, name)
VALUES (s.id, s.name)
"""
merchant_drop = "DROP TABLE IF EXISTS iceberg.order_source.merchant"

product_load_full = """\
MERGE INTO iceberg.order_source.product t
USING (
    SELECT id, merchant_id, price, amount, name
    FROM sourcedb.public.product
) s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET
    merchant_id = s.merchant_id,
    price = s.price,
    amount = s.amount,
    name = s.name
WHEN NOT MATCHED THEN INSERT (id, merchant_id, price, amount, name)
VALUES (s.id, s.merchant_id, s.price, s.amount, s.name)
"""
product_drop = "DROP TABLE IF EXISTS iceberg.order_source.product"

product_order_load_full = """\
MERGE INTO iceberg.order_source.product_order t
USING (
SELECT
    po.id AS product_order_id,
    po.amount,
    p.price,
    po.amount * p.price AS total_sum,
    po.order_id,
    po.product_id,
    p.merchant_id,
    co.customer_id
FROM sourcedb.public.customer_order co
JOIN sourcedb.public.product_order po ON po.order_id = co.id
JOIN sourcedb.public.product p ON p.id = po.product_id
) s ON t.product_order_id = s.product_order_id
WHEN MATCHED THEN UPDATE SET
    amount = s.amount, 
    price = s.price, 
    total_sum = s.total_sum, 
    order_id = s.order_id, 
    product_id = s.product_id, 
    merchant_id = s.merchant_id, 
    customer_id = s.customer_id
WHEN NOT MATCHED THEN INSERT (product_order_id, amount, price, total_sum, order_id, product_id, merchant_id, customer_id)
VALUES (s.product_order_id, s.amount, s.price, s.total_sum, s.order_id, s.product_id, s.merchant_id, s.customer_id)
"""
product_order_drop = "DROP TABLE IF EXISTS iceberg.order_source.product_order"

dbt_cleanup = [
    "DROP TABLE IF EXISTS iceberg.order_source.customer_fav_merchant",
    "DROP TABLE IF EXISTS iceberg.order_source.customer_spending_detail",
    "DROP VIEW IF EXISTS iceberg.order_source.customer_base",
    "DROP VIEW IF EXISTS iceberg.order_source.customer_loyalty",
    "DROP VIEW IF EXISTS iceberg.order_source.customer_spending",
    "DROP VIEW IF EXISTS iceberg.order_source.merchant_base",
    "DROP VIEW IF EXISTS iceberg.order_source.product_base",
    "DROP VIEW IF EXISTS iceberg.order_source.product_order_base",
    "DROP VIEW IF EXISTS iceberg.order_source.product_popularity",
    "DROP VIEW IF EXISTS iceberg.order_source.product_stock",
]
