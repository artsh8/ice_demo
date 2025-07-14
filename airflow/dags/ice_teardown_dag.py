from datetime import datetime
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import ice_common.operations as op


with DAG(
    dag_id="ice_teardown",
    start_date=datetime(2025, 7, 5),
    schedule="@once",
    catchup=False,
    max_active_runs=1,
) as dag:
    customer_drop = SQLExecuteQueryOperator(
        task_id="customer_drop", conn_id=op.CONN_TRINO, sql=op.customer_drop
    )
    merchant_drop = SQLExecuteQueryOperator(
        task_id="merchant_drop", conn_id=op.CONN_TRINO, sql=op.merchant_drop
    )
    product_drop = SQLExecuteQueryOperator(
        task_id="product_drop", conn_id=op.CONN_TRINO, sql=op.product_drop
    )
    product_order_drop = SQLExecuteQueryOperator(
        task_id="product_order_drop", conn_id=op.CONN_TRINO, sql=op.product_order_drop
    )
    dbt_cleanup = SQLExecuteQueryOperator(
        task_id="dbt_cleanup", conn_id=op.CONN_TRINO, sql=op.dbt_cleanup
    )
    order_source_schema_drop = SQLExecuteQueryOperator(
        task_id="order_source_schema_drop",
        conn_id=op.CONN_TRINO,
        sql=op.order_source_schema_drop,
    )

    (
        [customer_drop, merchant_drop, product_drop, product_order_drop]
        >> dbt_cleanup
        >> order_source_schema_drop
    )
