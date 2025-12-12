#!/usr/bin/env python
import os
import sys
from kafka import KafkaConsumer
bootstrap_servers = os.environ['KAFKA_BOOTSTRAP_SERVERS']
topic = os.environ['KAFKA_TOPIC']
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)
sys.stdout.write ("listening...\n")
sys.stdout.flush()
for msg in consumer:
    sys.stdout.write (msg.key.decode() + ":" + msg.value.decode() + "\n")
    sys.stdout.flush()
