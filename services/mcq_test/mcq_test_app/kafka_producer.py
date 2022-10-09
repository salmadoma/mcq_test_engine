"""store data into kafka"""

import logging
import os
from typing import List
from werkzeug.exceptions import InternalServerError

from json import dumps

from kafka import KafkaProducer

logger = logging.getLogger('kafka_producer.py')
logger.setLevel(os.getenv('LOGGING_LEVEL'))
producer = None


def create_producer():
    """
    Creates a kafka producer.

    :return: a kafka producer
    """

    global producer

    if producer is not None:
        return

    broker = os.getenv('CONFLUENT_KAFKA_BROKERS')

    # Create a Producer
    producer = KafkaProducer(
        bootstrap_servers=[broker],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )


def store_in_kafka(data: List[dict], topic: str) -> int:
    """
    Store data into a kafka topic.

    :return: Number of messages still in the Producer queue.
    :raises InternalServerError
    """

    if producer is None:
        logger.info("create Kafka producer")
        create_producer()

    try:
        producer.send(topic, value=data)

    except Exception as ex:
        logger.error('Producing failed: %s', str(ex))
        raise InternalServerError(description="Failed to send data to Kafka")

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    return producer.flush()