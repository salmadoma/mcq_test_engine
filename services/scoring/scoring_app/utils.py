import math

from .models import *
from .kafka_consumer import *

quiz_kafka_topic =os.getenv('KAFKA_TOPIC', "quiz")


def _update_quiz_score(data):
    score = _calc_score(data)
    Quiz.objects.update_or_create(topic=data.get("topic"), student=data.get("student"), defaults={"score": score})


def _calc_score(quiz):
    num_of_questions: int = quiz.get("num_of_questions")
    marked_answers: dict = quiz.get("marked_answers")
    num_of_correct_answers: int = sum(marked_answers.values())
    score: int = math.ceil((num_of_correct_answers / num_of_questions) * 100)
    return score


def _score():
    consumer = kafka_consumer(quiz_kafka_topic)
    for event in consumer:
        if event.value:
            _update_quiz_score(event.value[0])
