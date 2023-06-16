from datetime import timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from src.Snowflake.snowflake import SnowflakeQuery


args = {
    'owner': 'Airflow',
    'start_date': days_ago(1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email': ['global-de@gameloft.com'],
    'email_on_failure': True,
}

dag = DAG(
    'schedule_snowflake_queries_dag',
    default_args=args,
    description='Schedule Snowflake Queries DAG',
    schedule_interval='0 0 * * *'
)

with dag:

    # In the documentation of my airflow (v2.6.1), the Dummy operator is EmptyOperator
    start_task = EmptyOperator(
        task_id='start_task'
    )

    import_user_data_task = PythonOperator(
        task_id='import_user_data_task',
        python_callable=SnowflakeQuery.query,
        op_kwargs={'query': '<TO BE FILLED>'},
    )

    import_currency_conversion_task = PythonOperator(
        task_id='import_currency_conversion_task',
        python_callable=SnowflakeQuery.query,
        op_kwargs={'query': '<TO BE FILLED>'},
    )

    aggregate_transaction_task = PythonOperator(
        task_id='aggregate_transaction_task',
        python_callable=SnowflakeQuery.query,
        op_kwargs={'query': '<TO BE FILLED>'},
    )

    end_task = EmptyOperator(
        task_id='end_task'
    )

    (
        start_task
        >> [import_user_data_task, import_currency_conversion_task]
        >> aggregate_transaction_task
        >> end_task
    )



