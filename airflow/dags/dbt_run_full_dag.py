from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from ice_common.operations import DBT_PROJECT_DIR, DBT_PROFILE_DIR

with DAG(
    dag_id="dbt_run_full",
    start_date=datetime(2025, 7, 5),
    schedule="@once",
    catchup=False,
    max_active_runs=1,
) as dag:
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILE_DIR}",
    )
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILE_DIR}",
    )

    dbt_run >> dbt_test
