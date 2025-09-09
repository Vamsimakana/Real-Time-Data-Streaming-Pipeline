# producer/producer.py
import json, time, random
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=["localhost:9092"],
                         value_serializer=lambda v: json.dumps(v).encode("utf-8"))

TOPIC = "events"

def gen_event():
    return {
        "user_id": f"user_{random.randint(1,50)}",
        "event_type": random.choice(["click","view","purchase"]),
        "value": round(random.random()*100,2),
        "ts": int(time.time()*1000)
    }

if __name__ == "__main__":
    print("Producing events to Kafka topic 'events' ...")
    i = 0
    while True:
        ev = gen_event()
        producer.send(TOPIC, ev)
        i += 1
        if i % 100 == 0:
            producer.flush()
        time.sleep(0.05)  # ~20 events/sec
