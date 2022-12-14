import math
import threading
from typing import List

from .models import *
from .kafka_consumer import *

quiz_kafka_topic = os.getenv('KAFKA_TOPIC', "quiz")
quiz_thread = None


def _update_quiz_score(data: dict):
    """ Update quiz score in database

    :param data: quiz data
    """
    score = _calc_score(data)
    Quiz.objects.update_or_create(topic=data.get("topic"), student=data.get("student"), defaults={"score": score})


def _calc_score(quiz: dict):
    """ Calculate quiz score.

    :param quiz: quiz data
    :return score: quiz score.
    """
    num_of_questions: int = quiz.get("num_of_questions")
    marked_answers: dict = quiz.get("marked_answers")
    num_of_correct_answers: int = sum(marked_answers.values())
    score: int = math.ceil((num_of_correct_answers / num_of_questions) * 100)
    return score


def _score():
    """ Score Quiz data retrieved from kafka topic .
    """
    consumer = kafka_consumer(quiz_kafka_topic)
    for event in consumer:
        if event.value:
            _update_quiz_score(event.value[0])


def calc_avg(data: List[dict], key: str):
    """ Calculate average of selected field.

    :param data: data to be iterated over
    :param key: selected key.
    :return : average.
    """
    count = len(data)
    sum = 0
    for item in data:
        sum += item.get(key)
    return math.ceil(sum / count)


def calc_max(data: List[dict], key: str):
    """ Calculate max of selected field.

    :param data: data to be iterated over
    :param key: selected key.
    :return : max.
    """
    max = 0
    max_item = None
    for item in data:
        value = item.get(key)
        if value > max:
            max = value
            max_item = item
    return max_item


def init_quiz_thread():
    """ Initialize quiz thread to consume from kafka if it is not initialize before.
    """
    global quiz_thread
    if not quiz_thread:
        thread = threading.Thread(target=_score)
        thread.start()
