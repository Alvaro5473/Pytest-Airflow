FROM apache/airflow
COPY dags/ /opt/airflow/dags/
COPY config/ /opt/airflow/config/