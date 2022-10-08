import random

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers as core_serializers

from .models import *
from .serializers import *


# 1- submit: partial submit of quiz with the one correct answer


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
    # checking for the parameters from the URL
    try:
        topic = Topic.objects.get(id=_id)
        data = TopicSerializer(topic, many=False)
        return Response(data.data)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_topic(request):
    topic = TopicSerializer(data=request.data)
    if topic.is_valid():
        topic.save()
        return Response(topic.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_topic(request, _id):
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
    # checking for the parameters from the URL
    try:
        question = Question.objects.get(id=_id)
        data = QuestionSerializer(question, many=False)
        return Response(data.data)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_question(request):
    question = QuestionSerializer(data=request.data)
    if question.is_valid():
        question.save()
        return Response(question.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_question(request, _id):
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
    # checking for the parameters from the URL
    try:
        answer = Answer.objects.get(id=_id)
        data = AnswerSerializer(answer, many=False)
        return Response(data.data)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_answer(request):
    answer = AnswerSerializer(data=request.data)
    if answer.is_valid():
        answer.save()
        return Response(answer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_answer(request, _id):
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
    # checking for the parameters from the URL
    try:
        student = Student.objects.get(id=_id)
        data = StudentSerializer(student, many=False)
        return Response(data.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_student(request):
    # # # validating for already existing data
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
    result = {}
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
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def submit(request):
    print(request.data)
    return Response({"testt": 1})
    # result = {}
    # quiz = QuizSerializer(data=request.data)
    # if quiz.is_valid():
    #     quiz.save()
    #     questions = list(Topic.objects.get(id=request.data.get("topic")).get_questions())
    #     random.shuffle(questions)
    #     for idx, question in enumerate(questions):
    #         answers = list(question.get_answers())
    #         random.shuffle(answers)
    #         result[str(question)] = list(map(str, answers))
    #     return Response(result)
    # else:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

# endregion