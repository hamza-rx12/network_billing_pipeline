FROM flink:1.17.0-scala_2.12-java11

COPY ./jars/* /opt/flink/lib/

RUN chown -R flink:flink /opt/flink/lib
ENV TASK_MANAGER_NUMBER_OF_TASK_SLOTS=4
