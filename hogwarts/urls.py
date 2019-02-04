"""hogwarts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('select2/', include('django_select2.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sortinghat/', include('sortinghat.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('survey_statistics/', views.survey_statistics, name='survey_statistics'),
    path('available_courses/', views.available_courses, name='available_positions'),
    path('getCourseInfo/', views.getCourseInfo, name='getCourseInfo'),
    path('view_students/', views.view_students, name='view_students'),
    path('getSurveyProgress/', views.getSurveyProgress, name='getSurveyProgress'),
    path('getStudentStats/', views.getStudentStats, name='getStudentStats'),
]
