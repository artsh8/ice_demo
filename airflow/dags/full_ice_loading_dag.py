from datetime import datetime
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import ice_common.operations as op


with DAG(
    dag_id="full_ice_loading",
    start_date=datetime(2025, 7, 5),
    schedule="@once",
    catchup=False,
    max_active_runs=1,
) as dag:
    order_source_schema_create = SQLExecuteQueryOperator(
        task_id="order_source_schema_create",
        conn_id=op.CONN_TRINO,
        sql=op.order_source_schema_create,
    )
    all_tables_create = SQLExecuteQueryOperator(
        task_id="all_tables_create", conn_id=op.CONN_TRINO, sql=op.all_tables_create
    )
    customer_load_full = SQLExecuteQueryOperator(
        task_id="customer_load_full", conn_id=op.CONN_TRINO, sql=op.customer_load_full
    )
    merchant_load_full = SQLExecuteQueryOperator(
        task_id="merchant_load_full", conn_id=op.CONN_TRINO, sql=op.merchant_load_full
    )
    product_load_full = SQLExecuteQueryOperator(
        task_id="product_load_full", conn_id=op.CONN_TRINO, sql=op.product_load_full
    )
    product_order_load_full = SQLExecuteQueryOperator(
        task_id="product_order_load_full",
        conn_id=op.CONN_TRINO,
        sql=op.product_order_load_full,
    )

    (
        order_source_schema_create
        >> all_tables_create
        >> [
            customer_load_full,
            merchant_load_full,
            product_load_full,
            product_order_load_full,
        ]
    )
