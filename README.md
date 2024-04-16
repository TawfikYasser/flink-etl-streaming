# flink-etl-streaming
ETL using Flink, Kafka, PostgreSQL, Elasticsearch, and Kibana

* Running the docker-compose.yml to setup the containers.
* check if kafka is correct running:
kafka-topics --list --bootstrap-server broker:9092
* Create the data generator using the main.py
* Install confluent kafka module
* Install simplejson module
* Check if kafka is running:
    - docker exec -it broker /bin/bash
    - kafka-topics --list --bootstrap-server broker:9092
* Write the main.py code to produce to kafka topic.
* Test and consume using: kafka-console-consumer --topic financial_transactions --bootstrap-server broker:29092 --from-beginning
* Create a new project in intelliJ Idea for Flink part to consume the data from kafka.
    - Choose maven archtype from the left side menu
    - add the project name and path
    - Choose 'Maven Centeral' as catalog
    - in the archtype choose `org.apache.flink:flink-quickstart-java`
    - Advanced -> GroupId: FlinkETLStreaming

* Adding in pom.xml the dependinces of kafka, postgresql, and elasticsearch so that flink can connect with them

		<dependency>
			<groupId>org.apache.flink</groupId>
			<artifactId>flink-connector-kafka</artifactId>
			<version>3.0.1-1.18</version>
		</dependency>

		<dependency>
			<groupId>org.postgresql</groupId>
			<artifactId>postgresql</artifactId>
			<version>42.6.0</version>
		</dependency>

		<dependency>
			<groupId>org.apache.flink</groupId>
			<artifactId>flink-sql-connector-elasticsearch7</artifactId>
			<version>3.0.1-1.17</version>
		</dependency>


* Starting building the project with classes and pipeline.
* After writing the pipeline we need to download the source of flink 1.18, extract it using `tar -zxvf`.
* Then start flink cluster using ./bin/start-cluster.sh
* Then use maven to compile and build the project and submit it to the cluster.
* The error: 
Caused by: com.fasterxml.jackson.databind.exc.UnrecognizedPropertyException: Unrecognized field "transactionId" (class FlinkETLStreaming.Dto.Transaction), not marked as ignorable (0 known properties: ])

because no setters and getters, we will use `import lombok.Data;`
Now the job is running

* Now we need to connect to postgres from flink, we will add the following dependency for the JDBCSink
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-connector-jdbc</artifactId>
            <version>3.1.1-1.17</version>
        </dependency>

* Writing the jdbc sink for creating and inserting data into the transactions table, now rebuild and run the pipeline to check if the database contains what we want.

* Now we want to have 3 sinks, transactions by category, day, and month.
* After writing the code, rebuild, submit to the cluster, check in postgres.

* Now work on kibana and elasticsearch
* Writing the Elasticsearch sink.
* rebuild ad rsubmit to check

it works, data in elasticsearch

GET transactions/_search

* For dashboard go to the Dashboard section on the left side menu.
