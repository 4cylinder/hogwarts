from django.urls import path

from . import views

app_name = 'sortinghat'
urlpatterns = [
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('student_survey', views.student_survey, name='student_survey'),
	path('student_submit', views.student_submit, name='student_submit'),
    path('professor_survey', views.professor_survey, name='professor_survey'),
    path('professor_submit', views.professor_submit, name='professor_submit'),
]