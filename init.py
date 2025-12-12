#!/usr/bin/env python
import os
import time

from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import NoBrokersAvailable, TopicAlreadyExistsError

# time.sleep(5)

bootstrap_servers = os.environ['KAFKA_BOOTSTRAP_SERVERS']
topics = os.environ['KAFKA_TOPICS']

client: KafkaAdminClient
try:
    client = KafkaAdminClient(bootstrap_servers=bootstrap_servers,
        security_protocol='SSL',
        ssl_cafile='/opt/kafka/ssl/rootCA.pem',
    )
except NoBrokersAvailable:
    print ("Not ready")
    exit(1)

new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in topics.split(",")]

try:
    client.create_topics(new_topics)
except TopicAlreadyExistsError:
    print ("Topic already exists, nothing to do")
    exit(0)
