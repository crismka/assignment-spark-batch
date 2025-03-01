from datetime import timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "dibimbing",
    "retry_delay": timedelta(minutes=5),
}

spark_dag = DAG(
    dag_id="assignment",
    default_args=default_args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60),
    description="Assignment",
    start_date=days_ago(1),
)

Extract = SparkSubmitOperator(
    application="/spark-scripts/assignment.py",
    conn_id="spark_main",
    task_id="spark_submit_task",
    dag=spark_dag,
    packages = 'org.postgresql:postgresql:42.2.18'
)

Extract
