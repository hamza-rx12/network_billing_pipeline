from kafka import KafkaProducer
import json
import time
from datetime import datetime, timedelta
import random

# Kafka configuration
KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "voice_records"

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def generate_record():
    """Generate a random voice record."""
    record = {
        "record_type": "voice",
        "timestamp": (
            datetime.utcnow() - timedelta(seconds=random.randint(0, 3600))
        ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "caller_id": f"2126{random.randint(10000000, 99999999)}",
        "callee_id": f"2126{random.randint(10000000, 99999999)}",
        "duration_sec": random.randint(1, 600),
        "cell_id": f"ALHOCEIMA_{random.randint(1, 50)}",
        "technology": random.choice(["3G", "4G", "5G"]),
    }
    return record


def produce_data():
    """Produce data to Kafka topic."""
    try:
        while True:
            record = generate_record()
            producer.send(TOPIC_NAME, record)
            print(f"Produced: {record}")
            time.sleep(1)  # Adjust the sleep time as needed
    except KeyboardInterrupt:
        print("Stopping producer...")
    finally:
        producer.close()


if __name__ == "__main__":
    produce_data()
