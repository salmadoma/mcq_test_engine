from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('student-result-in-topic', views.student_result_in_topic,
         name='student-result-in-topic'),
    path('student-average-in-all-topics', views.student_average_in_all_topics,
         name='student-average-in-all-topics'),
    path('average-result-in-topic', views.average_result_in_topic,
         name='average-result-in-topic'),
    path('highest-score-in-topic', views.highest_score_in_topic,
         name='highest-score-in-topic')
]
