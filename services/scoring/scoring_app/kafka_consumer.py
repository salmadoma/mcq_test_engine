"""store data into kafka"""

import logging
import os

from kafka import KafkaConsumer
from json import loads
from werkzeug.exceptions import InternalServerError

logger = logging.getLogger('kafka_producer.py')
logger.setLevel(os.getenv('LOGGING_LEVEL'))


def kafka_consumer(topic: str):
    """ Consume kafka from specified topic.

    :param topic: topic name
    :return consumer: consumer object.
    """
    try:
        broker = os.getenv('CONFLUENT_KAFKA_BROKERS')
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=[broker],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group-id',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
        return consumer
    except Exception as ex:
        logger.error('Consuming failed: %s', str(ex))
        raise InternalServerError(description="Failed to send data to Kafka")
