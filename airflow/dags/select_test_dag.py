from datetime import datetime
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(
    dag_id="select_test",
    start_date=datetime(2025, 7, 5),
    schedule="@once",
    catchup=False,
    max_active_runs=1,
) as dag:
    select_test = SQLExecuteQueryOperator(
        task_id="select_test",
        conn_id="trino_default",
        sql="SELECT name FROM iceberg.order_source.merchant WHERE id = 56",
        requires_result_fetch=True,
    )
    select_test
