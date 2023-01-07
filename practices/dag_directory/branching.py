# start: IMPORTING
## airflow
from airflow                  import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
## general
import random

from datetime import datetime, timedelta
# end: IMPORTING

# start: DEFINNING TOOL FUNCTIONS
def _generate_accuracy(ti):
    """Generates a random value between 0 and 1 and
    pushes it as XCOM into Airlfow"""
    random_accuracy = random.uniform(0,1)

    ti.xcom_push(key='model_accuracy', value=random_accuracy)


def _check_accuracy(ti):
    """Reads Airflow XCOMs looking for a model_accuracy key and
    check its value"""
    accuracy = ti.xcom_pull(key='model_accuracy')

    if accuracy >= 0.8:
        return 'deploy_task'
    else:
        return 'retrain_task'

# end: DEFINNING TOOL FUNCTIONS


# start: DEFINNING THE DAG
with DAG(
    dag_id = 'branching_test',
    description='Testing flow managing with branching',
    schedule_interval=timedelta(minutes=2),
    start_date=datetime(2023,1,1),
    catchup=False
) as dag:

    get_accuracy_op = PythonOperator(
        task_id='get_accuracy_task',
        python_callable=_generate_accuracy
    )

    check_accuracy_op = BranchPythonOperator(
        task_id='check_accuracy_task',
        python_callable=_check_accuracy
    )

    deploy_op = DummyOperator(
        task_id='deploy_task'
    )

    retrain_op = DummyOperator(
        task_id='retrain_task'
    )

    get_accuracy_op >> check_accuracy_op >> [deploy_op, retrain_op]
# end: DEFINNING THE DAG