from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from ice_common.operations import DBT_PROJECT_DIR, DBT_PROFILE_DIR, DBT_MARTS_DIR

with DAG(
    dag_id="dbt_run_marts",
    start_date=datetime(2025, 7, 5),
    schedule="@once",
    catchup=False,
    max_active_runs=1,
) as dag:
    dbt_run_marts = BashOperator(
        task_id="dbt_run_marts",
        bash_command=f"dbt run -s +{DBT_MARTS_DIR} --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILE_DIR}"
    )
    
    dbt_run_marts
