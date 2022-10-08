from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 4- get result of quiz for one student and one topic
# 5- get average of quiz for one topic
# 6- get highest score of quiz for one topic
# 7- get average of quiz for one student in all topics

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
    student = request.query_params.get('student')
    topic = request.query_params.get('topic')
    print(student)
    print(topic)
    return Response("successes")


@api_view(['GET'])
def student_average_in_all_topics(request):
    student = request.query_params.get('student')
    print(student)
    return Response()


@api_view(['GET'])
def average_result_in_topic(request):
    topic = request.query_params.get('topic')
    print(topic)
    return Response()


@api_view(['GET'])
def highest_score_in_topic(request):
    topic = request.query_params.get('topic')
    print(topic)
    return Response()
