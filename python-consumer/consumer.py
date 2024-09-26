from kafka import KafkaConsumer
import redis
import os

KAFKA_BOOTSTRAP_SERVERS = os.environ.get(
    'KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
TOPIC_NAME = 'foo-topic'
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    group_id='python-consumer-group'
)

r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

for msg in consumer:
    print(f"Consumed message: {msg.value.decode('utf-8')}")
    r.incr('foo-counter')
    print(f"Updated Redis counter: {r.get('foo-counter').decode('utf-8')}")
