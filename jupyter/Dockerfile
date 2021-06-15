FROM jupyter/pyspark-notebook

USER root
RUN pip install findspark confluent_kafka pyspark flask nltk

USER jovyan

ENV JUPYTER_ENABLE_LAB="yes"

COPY ./jupyter/jars/spark-sql-kafka-0-10_2.12-3.0.0.jar /opt/conda/lib/python3.8/site-packages/pyspark/jars