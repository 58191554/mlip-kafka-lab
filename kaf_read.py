import os
from datetime import datetime
from json import dumps, loads
from time import sleep
from random import randint
from kafka import KafkaConsumer, KafkaProducer

# Update this for your own recitation section :)
topic = 'zhentong-test' # x could be b, c, d, e, f

# Create a consumer to read data from kafka
# Ref: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html

# [TODO]: Complete the missing ... parameters/arguments using the Kafka documentation
consumer = KafkaConsumer(
    topic, # the topic to subscribe to
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # Start reading from the beginning of the topic
    # Commit that an offset has been read
    enable_auto_commit=True,
    # How often to tell Kafka, an offset has been read
    auto_commit_interval_ms=1000
)

print('Reading Kafka Broker')
for message in consumer:
    message = message.value.decode()
    # Default message.value type is bytes!
    print(loads(message))
    os.system(f"echo {message} >> kafka_log.csv")