FROM python:3.11-slim

COPY constraints.txt constraints.txt
RUN pip install apache-airflow[trino]==2.11.0 -c constraints.txt
RUN pip install apache-airflow==2.11.0 dbt-core==1.8.2
RUN pip install apache-airflow==2.11.0 dbt-trino==1.8.2

WORKDIR /root/airflow
EXPOSE 8080

ENTRYPOINT ["airflow", "standalone"]
