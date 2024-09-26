from kafka import KafkaProducer
import os
import time

KAFKA_BOOTSTRAP_SERVERS = os.environ.get(
    'KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
TOPIC_NAME = 'input-topic'

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

messages = ['foo', 'bar', 'foo', 'baz', 'bar', 'foo']

for msg in messages:
    producer.send(TOPIC_NAME, msg.encode('utf-8'))
    print(f"Produced message: {msg}")
    time.sleep(1)

producer.flush()
