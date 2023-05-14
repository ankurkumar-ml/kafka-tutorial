from kafka import KafkaConsumer, KafkaProducer

def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def consume_message(topic_name):
    consumer = KafkaConsumer(topic_name,
                             auto_offset_reset="earliest",
                             bootstrap_servers = ['localhost:9092'],
                             api_version=(0, 10),
                             consumer_timeout_ms = 1000)

    for msg in consumer:
        print(msg.value)

    consumer.close()

# producer_instance = connect_kafka_producer()
# publish_message(producer_instance, "test_topic", "message_key", "message value")
# consume_message("test_topic")
