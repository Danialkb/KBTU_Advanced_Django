import confluent_kafka

from schemas import Film


producer = confluent_kafka.Producer(
    {"bootstrap.servers": "localhost:9092"}
)

topic = "main_topic"


def produce(film: Film) -> None:
    producer.produce(topic=topic, value=film.model_dump_json())
    producer.flush()


for i in range(5):
    produce(Film(name=f"name_{i + 1}", director="DIRECTOR"))
