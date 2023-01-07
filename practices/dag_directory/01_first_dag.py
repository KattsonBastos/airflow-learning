# IMPORTING
# airflow
from airflow                  import DAG
from airflow.operators.python import PythonOperator

# general
from datetime import datetime, timedelta

# this function is basically the task
def _print_hello():
    return 'Heey from our first DAG!!'

# creating the dag. It will be passed later to each task as \
## an argument to the 'dag' parameter
dag = DAG(
    dag_id = 'hello_world', # task_id
    description='Hello World DAG',
    schedule_interval=timedelta(minutes=1), # the interval in which the dag will be executed
    start_date=datetime(2023,1,1), # its a timestemp mainly used in the attempt t obackfill
    catchup=False # interval in which the DAG will try to execute again past paused runs
)

# python operator for the above function
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=_print_hello, # <-- here comes the 'hello' function we created
    dag=dag # <-- that's were the dag object we created comes in
)

# just calling our task
hello_task