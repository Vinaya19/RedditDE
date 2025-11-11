from airflow import DAG
from datetime import datetime
import os, sys
#from airflow.providers.standard.operators.python import PythonOperator
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline

# Defining a DAG
default_args = {
    'owner': 'Airflow Account Name',
    'start_date': datetime(2025, 6, 16)
}

dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    schedule='@daily',
    default_args=default_args,
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# Extracting data from Reddit
file_postfix = datetime.now().strftime("%Y%m%d")

extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = reddit_pipeline,
    op_kwargs = {
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable = upload_s3_pipeline,
    dag = dag
)

extract >> upload_s3