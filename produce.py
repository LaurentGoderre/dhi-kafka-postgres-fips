#!/usr/bin/env python
from datetime import datetime
import os
import sys
from kafka import KafkaProducer
bootstrap_servers = os.environ['KAFKA_BOOTSTRAP_SERVERS']
topic = os.environ['KAFKA_TOPIC']
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

value = "It is now: " + datetime.today().strftime('%Y-%m-%d %H:%M:%S')

producer.send(topic, key=b'foo', value=bytes(value, "utf-8"))
producer.flush()
producer.close()
