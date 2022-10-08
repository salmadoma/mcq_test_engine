from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),

    path('topics', views.list_topics, name='list-topics'),
    path('get-topic/<str:_id>', views.get_topic, name='get-topic'),
    path('create-topic', views.create_topic, name='create-topic'),
    path('update-topic/<str:_id>', views.update_topic, name='update-topic'),
    path('delete-topic/<str:_id>', views.delete_topic, name='delete-topic'),

    path('questions', views.list_questions, name='list-questions'),
    path('get-question/<str:_id>', views.get_question, name='get-question'),
    path('create-question', views.create_question, name='create-question'),
    path('update-question/<str:_id>', views.update_question, name='update-question'),
    path('delete-question/<str:_id>', views.delete_question, name='delete-question'),

    path('answers', views.list_answers, name='list-answers'),
    path('get-answer/<str:_id>', views.get_answer, name='get-answer'),
    path('create-answer', views.create_answer, name='create-answer'),
    path('update-answer/<str:_id>', views.update_answer, name='update-answer'),
    path('delete-answer/<str:_id>', views.delete_answer, name='delete-answer'),

    path('students', views.list_students, name='list-students'),
    path('get-student/<str:_id>', views.get_student, name='get-student'),
    path('create-student', views.create_student, name='create-student'),
    path('update-student/<str:_id>', views.update_student, name='update-student'),
    path('delete-student/<str:_id>', views.delete_student, name='delete-student'),

    path('enroll', views.enroll, name="enroll"),
    path('submit', views.submit, name="submit"),
]

