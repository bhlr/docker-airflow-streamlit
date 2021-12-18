import os

from airflow import DAG
from airflow.contrib.hooks.fs_hook import FSHook
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from structlog import get_logger
import pandas as pd

logger = get_logger()

COLUMNS = {
    "Province/State": "province",
    "Country/Region": "country",
    "Lat":"lat",
    "Long":"lon"
}

DATE_COLUMNS = ["ORDERDATE"]

FILE_CONNECTION_NAME = 'monitor_file'
CONNECTION_DB_NAME = 'mysql_db'

def etl_process(**kwargs):
    logger.info(kwargs["execution_date"])
    file_path = FSHook(FILE_CONNECTION_NAME).get_path()
    filename = 'time_series_covid19_recovered_global.csv'
    mysql_connection = MySqlHook(mysql_conn_id=CONNECTION_DB_NAME).get_sqlalchemy_engine()
    full_path = f'{file_path}/{filename}'
    df = (pd.read_csv(full_path, encoding = "ISO-8859-1")
          .rename(columns=COLUMNS)
          )

    df = df.melt(id_vars=["province", "country","lat","lon"], 
        var_name="date", 
        value_name="cases")

    df['date'] = pd.to_datetime(df['date'],format='%m/%d/%y')

    df["type"] = 'r'

    with mysql_connection.begin() as connection:
        connection.execute("DELETE FROM test.covid19_cases WHERE type='r'")
        df.to_sql('covid19_cases', con=connection, schema='test', if_exists='append', index=False)

    os.remove(full_path)

    logger.info(f"Rows inserted {len(df.index)}")





dag = DAG('covid19_recovered_ingestion_dag', description='Dag to Ingest COVID19 recovered',
          default_args={
              'owner': 'byron.linares',
              'depends_on_past': False,
              'max_active_runs': 1,
              'start_date': days_ago(5)
          },
          schedule_interval='* * * * *',
          catchup=False)

sensor = FileSensor(task_id="file_sensor_task",
                    dag=dag,
                    filepath='time_series_covid19_recovered_global.csv',
                    fs_conn_id=FILE_CONNECTION_NAME,
                    poke_interval=10,
                    timeout=600)

etl = PythonOperator(task_id="covid19Recov_etl",
                     provide_context=True,
                     python_callable=etl_process,
                     dag=dag
                     )

sensor >> etl
