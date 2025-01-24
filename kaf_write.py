import os
from datetime import datetime
from json import dumps, loads
from time import sleep
from random import randint
from kafka import KafkaConsumer, KafkaProducer

# Update this for your own recitation section :)
topic = 'zhentong-test' # x could be b, c, d, e, f

# Create a producer to write data to kafka
# Ref: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html

# [TODO]: Replace '...' with the address of your Kafka bootstrap server
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x: dumps(x).encode('utf-8'))

# [TODO]: Add cities of your choice
cities = [
    'New York',
    'Los Angeles',
    'Chicago',
    'Houston',
    'Phoenix',
    'Philadelphia',
    'San Antonio',
    'San Diego',
    'Dallas',
    'San Jose',
    'Austin',
    'Jacksonville',
    'San Francisco',
    'Columbus',
    'Charlotte',
    'Seattle'
]

# Write data via the producer
print("Writing to Kafka Broker")
while True:
    data = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")},{cities[randint(0,len(cities)-1)]},{randint(18, 32)}ºC'
    print(f"Writing: {data}")
    producer.send(topic=topic, value=data)
    input("Press Enter to continue...")