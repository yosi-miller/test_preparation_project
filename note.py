# Kafka architecture
"""
- Brokers - server that store and forward messages
- Topics - Categories or feed names that the messages are published to
- Partition - splits of a topic for parallelism
- Producers and Consumers - applications that write data to and read from kafka
- zookeeper - service that coordinates kafka brokers
"""

# pip install kafka-python

# docker-compose up -d

# how to create a topic:
"""
1. access the container

docker exec -it kafka_teaching_2-kafka-1 bash

2. create the topic

kafka-topics --create --topic gur_topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

kafka-topics --create --topic random-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

kafka-topics --create --topic finsh_topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3

excpeted output: Created topic gur_topic.
"""

# how do i know what topics do i have?
"""
kafka-topics --list --bootstrap-server localhost:9092
"""

# how to produce message
"""
kafka-console-producer --topic gur_topic --bootstrap-server localhost:9092
"""


# how to consume message
"""
kafka-console-consumer --topic gur_topic --from-beginning --bootstrap-server localhost:9092
"""