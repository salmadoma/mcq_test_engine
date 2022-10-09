import logging
import os
import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .kafka_producer import store_in_kafka

logger = logging.getLogger('mcq_test_app')
logger.setLevel(os.getenv('LOGGING_LEVEL'))
quiz_kafka_topic = os.getenv('KAFKA_TOPIC', "quiz")


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'All topics': '/topics',
        'Create topic': '/create-topic',
        'Update topic': '/update-topic/id',
        'Delete topic': '/delete-topics/id',
        'All questions': '/questions',
        'Create question': '/create-question',
        'Update question': '/update-question/id',
        'Delete question': '/delete-question/id',
        'All answers': '/answers',
        'Create answer': '/create-answer',
        'Update answer': '/update-answer/id',
        'Delete answer': '/delete-answer/id',
        'All students': '/students',
        'Create student': '/create-student',
        'Update student': '/update-student/id',
        'Delete student': '/delete-student/id',
        'Enroll': '/enroll',
        'Submit': '/submit'
    }

    return Response(api_urls)


# region Topics

@api_view(['GET'])
def list_topics(request):
    """ List all topics.

    :param request: request object
    :return Response: Response object.
    """
    # checking for the parameters from the URL
    if request.query_params:
        topics = Topic.objects.filter(**request.query_param.dict())
    else:
        topics = Topic.objects.all()
    if topics:
        data = TopicSerializer(topics, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_topic(request, _id):
    """ Get topic by id.

    :param request: request object
    :return Response: Response object.
    """
    # checking for the parameters from the URL
    try:
        topic = Topic.objects.get(id=_id)
        data = TopicSerializer(topic, many=False)
        return Response(data.data)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_topic(request):
    """ Create topic.

    :param request: request object
    :return Response: Response object.
    """
    topic = TopicSerializer(data=request.data)
    if topic.is_valid():
        topic.save()
        return Response(topic.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_topic(request, _id):
    """ Update topic by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    try:
        topic = Topic.objects.get(id=_id)
        topic_serializer = TopicSerializer(instance=topic, data=request.data, partial=True)
        if topic_serializer.is_valid():
            topic_serializer.save()
            return Response(topic_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_topic(request, _id):
    """ Delete topic by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    try:
        topic = Topic.objects.get(id=_id)
        topic.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# endregion

# region Questions

@api_view(['GET'])
def list_questions(request):
    """ List all topics.

    :param request: request object
    :return Response: Response object.
    """
    # checking for the parameters from the URL
    if request.query_params:
        questions = Question.objects.filter(**request.query_param.dict())
    else:
        questions = Question.objects.all()
    if questions:
        data = QuestionSerializer(questions, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_question(request, _id):
    """ Get question by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    # checking for the parameters from the URL
    try:
        question = Question.objects.get(id=_id)
        data = QuestionSerializer(question, many=False)
        return Response(data.data)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_question(request):
    """ Create question.

    :param request: request object
    :return Response: Response object.
    """
    question = QuestionSerializer(data=request.data)
    if question.is_valid():
        question.save()
        return Response(question.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_question(request, _id):
    """ Update question by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    try:
        question = Question.objects.get(id=_id)
        question_serializer = QuestionSerializer(instance=question, data=request.data, partial=True)
        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_question(request, _id):
    """ Delete question by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    try:
        question = Question.objects.get(id=_id)
        question.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# endregion

# region Answers

@api_view(['GET'])
def list_answers(request):
    """ List all answers.

    :param request: request object
    :return Response: Response object.
    """
    # checking for the parameters from the URL
    if request.query_params:
        answers = Answer.objects.filter(**request.query_param.dict())
    else:
        answers = Answer.objects.all()
    if answers:
        data = AnswerSerializer(answers, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_answer(request, _id):
    """ Get answer by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    # checking for the parameters from the URL
    try:
        answer = Answer.objects.get(id=_id)
        data = AnswerSerializer(answer, many=False)
        return Response(data.data)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_answer(request):
    """ Create answer.

    :param request: request object
    :return Response: Response object.
    """
    answer = AnswerSerializer(data=request.data)
    if answer.is_valid():
        answer.save()
        return Response(answer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_answer(request, _id):
    """ Update answer by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    try:
        answer = Answer.objects.get(id=_id)
        answer_serializer = AnswerSerializer(instance=answer, data=request.data, partial=True)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response(answer_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_answer(request, _id):
    """ Delete answer by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    try:
        answer = Answer.objects.get(id=_id)
        answer.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# endregion

# region Students

@api_view(['GET'])
def list_students(request):
    """ List all students.

    :param request: request object
    :return Response: Response object.
    """
    # checking for the parameters from the URL
    if request.query_params:
        students = Student.objects.filter(**request.query_param.dict())
    else:
        students = Student.objects.all()
    if students:
        data = StudentSerializer(students, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_student(request, _id):
    """ Get student by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    # checking for the parameters from the URL
    try:
        student = Student.objects.get(id=_id)
        data = StudentSerializer(student, many=False)
        return Response(data.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_student(request):
    """ Create student.

    :param request: request object
    :return Response: Response object.
    """
    #  validating for already existing data
    if Student.objects.filter(phone=request.data.get("phone")):
        return Response({"error": "This phone already exists"})
    student = StudentSerializer(data=request.data)

    if student.is_valid():
        student.save()
        return Response(student.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_student(request, _id):
    """ Update student by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    try:
        student = Student.objects.get(id=_id)
        student_serializer = StudentSerializer(instance=student, data=request.data, partial=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_student(request, _id):
    """ Delete student by id.

    :param request: request object
    :param _id: object _id
    :return Response: Response object.
    """
    try:
        student = Student.objects.get(id=_id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# endregion

# region MCQ test


@api_view(['POST'])
def enroll(request):
    """ Enroll in exam for specific student with specific topic.

    :param request: request object
    :return Response: Response object with shuffled questions and answers.
    """
    result = {}
    try:
        Quiz.objects.get(topic=request.data.get("topic"), student=request.data.get("student"))
    except Quiz.DoesNotExist:
        quiz = QuizSerializer(data=request.data)
        if quiz.is_valid():
            quiz.save()

    questions = list(Topic.objects.get(id=request.data.get("topic")).get_questions())
    random.shuffle(questions)
    for idx, question in enumerate(questions):
        answers = list(question.get_answers())
        random.shuffle(answers)
        result[str(question)] = list(map(str, answers))
    return Response(result)


@api_view(['POST'])
def submit(request):
    """ Submit exam answers for specific student with specific topic.

    :param request: request object
    :return Response: Response object with marked answers.
    """
    student = request.data.get('student')
    topic = request.data.get('topic')
    answers = request.data.get('answers')
    try:
        num_of_questions, marked_answers = _mark_quiz(topic, answers)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    quiz = [
        {"student": student, "topic": topic, "num_of_questions": num_of_questions, "marked_answers": marked_answers}]
    store_in_kafka(quiz, quiz_kafka_topic)
    logger.info(f"data pushed into kafka topic: {quiz_kafka_topic}")
    return Response(quiz)


def _mark_quiz(topic, answers):
    """ Mark student exam for specific topic.

    :param topic: topic id
    :param answers: Submitted answers for each question.
    :return num_of_questions: Number of question in the current exam.
    :return marked_answers: Marked answers of question in the current exam.
    """
    questions = Topic.objects.get(id=topic).get_questions()
    num_of_questions = len(questions)
    marked_answers = {}
    for answer in answers.values():
        answer_object = Answer.objects.get(id=answer)
        marked_answers[answer] = answer_object.correct
    return num_of_questions, marked_answers

# endregion
