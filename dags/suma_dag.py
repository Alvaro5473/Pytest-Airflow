# suma_dag.py
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from sumador import sumar

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG('suma_dag', default_args=default_args, schedule_interval=None)

def tarea_suma():
    resultado = sumar(2, 3)
    print("El resultado de la suma es:", resultado)

tarea_python = PythonOperator(
    task_id='ejecutar_suma',
    python_callable=tarea_suma,
    dag=dag
)

tarea_bash = BashOperator(
    task_id='imprimir_resultado',
    bash_command='echo El resultado es: {{ task_instance.xcom_pull(task_ids="ejecutar_suma") }}',
    dag=dag
)

tarea_python >> tarea_bash
