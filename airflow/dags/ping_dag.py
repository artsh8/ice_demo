from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def ping():
    print("pong")


with DAG(
    dag_id="ping",
    start_date=datetime(2025, 7, 5),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
) as dag:
    check_ping = PythonOperator(task_id="check_ping", python_callable=ping)
    check_ping
