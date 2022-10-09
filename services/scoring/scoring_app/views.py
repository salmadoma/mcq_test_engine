import logging
import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .utils import init_quiz_thread, calc_avg, calc_max

logger = logging.getLogger('scoring_app')
logger.setLevel(os.getenv('LOGGING_LEVEL'))


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Student’s result in topic': '/student-result-in-topic',
        'Student’s average in all topics': '/student-average-in-all-topics',
        'Average result in a topic': '/average-result-in-topic',
        'Highest score in a topic': '/highest-score-in-topic',
    }

    return Response(api_urls)


@api_view(['GET'])
def student_result_in_topic(request):
    """ Calculate Student’s result in specific topic.

    :param request: request object
    :return Response: Response object with quiz data.
    """
    student = request.query_params.get('student')
    topic = request.query_params.get('topic')
    try:
        init_quiz_thread()
        quiz = Quiz.objects.get(student=student, topic=topic)
        quiz = QuizSerializer(quiz, many=False)
        logger.info(f"quiz data: {quiz} retrieved successfully")
        return Response(quiz.data)
    except Quiz.DoesNotExist:
        logger.error(f"quiz does not exist")
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def student_average_in_all_topics(request):
    """ Calculate Student’s average result in all topics.

    :param request: request object
    :return Response: Response object with quiz data.
    """
    student = request.query_params.get('student')
    init_quiz_thread()
    quiz_objects = Quiz.objects.filter(student=student)
    if quiz_objects:
        quizzes = QuizSerializer(quiz_objects, many=True)
        avg = calc_avg(quizzes.data, "score")
        logger.info(f"quiz data: {quizzes} retrieved successfully")
        return Response({"student": student, "average": avg})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def average_result_in_topic(request):
    """ Calculate topic’s average result.

    :param request: request object
    :return Response: Response object with quiz data.
    """
    topic = request.query_params.get('topic')
    init_quiz_thread()
    quiz_objects = Quiz.objects.filter(topic=topic)
    if quiz_objects:
        quizzes = QuizSerializer(quiz_objects, many=True)
        avg = calc_avg(quizzes.data, "score")
        return Response({"topic": topic, "average": avg})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def highest_score_in_topic(request):
    """ Calculate topic’s highest_score for all exams.

    :param request: request object
    :return Response: Response object with quiz data.
    """
    topic = request.query_params.get('topic')
    init_quiz_thread()
    quiz_objects = Quiz.objects.filter(topic=topic)
    if quiz_objects:
        quizzes = QuizSerializer(quiz_objects, many=True)
        highest_quiz_score = calc_max(quizzes.data, "score")
        return Response(highest_quiz_score)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
