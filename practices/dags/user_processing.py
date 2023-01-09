"""
Practicing DAG parameters: creating our first DAG
"""

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import datetime

with DAG(
    'user_processing',
    start_date=datetime(2023,1,1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    create_table_op = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
            )
        '''
    )