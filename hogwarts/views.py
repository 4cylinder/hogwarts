from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json, mimetypes, os
from academics.models import *
from sortinghat.models import *

@login_required
def dashboard(request):
    # Professor dashboard
    if request.user.is_staff:
        return render(request, "dashboard/professor_dashboard.html", context={
            "semester": Semester.objects.get(active=True),
        })

    # Student dashboard
    # Get past courses (if applicable)
    pastCourses = Match.objects.filter(student=student)

    return render(request, "dashboard/student_dashboard.html", context={
        "semester": Semester.objects.get(active=True),
        "eligible": False,
        "pastCourses": pastCourses
    })

# For Professors only - stats for Sorting Hat Survey
@login_required
def survey_statistics(request):
    if request.user.is_staff:
        # Get all track sessions
        return render(request, "survey_statistics.html", context={"semesters": Semester.objects.all()})
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")

# See Student Details - Professors only
@login_required
def view_students(request):
    if request.user.is_staff:
        students = User.objects.filter(groups__name="Students")
        return render(request, "view_students.html", context={"students": students})
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")

# See Course Details (Students)
@login_required
def available_courses(request):
    houses = JobFunction.objects.all().order_by("function_text")
    coursesByHouse = {}
    for house in houses:
        coursesByHouse[house.house_name] = []
        courses = Course.objects.filter(house=house, active=True).order_by("course_name")
        for course in courses:
            coursesByHouse[house.house_name].append({"id": course.id, "course_name": course.course_name})

    return render(request, "available_courses.html", context={
        "coursesByHouse": coursesByHouse,    
    })

# For Students viewing all available courses. Load on demand via AJAX to save time on initial page load
@login_required
def getCourseInfo(request):
    cid = request.POST.get('cid')
    try:
        course = Course.objects.get(pk=pid)
        data = {
            "status": "success",
            "house": course.house.house_name,
            "course_name": course.course_name,
            "professor": "%s %s (%s)" % (course.professor.first_name, course.professor.last_name, course.professor.email),
            "floor": course.floor,
            "classroom": course.classroom,
            "description": position.description.replace("\n","<br/>"),
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        return HttpResponseBadRequest()

# For Professor dashboard pie chart that shows how many Students did the latest survey
@login_required
def getSurveyProgress(request):
    try:
        semester = Semester.objects.get(is_active=True)
        numStudents = len(User.objects.filter(groups__name="Students"))
        filled = HouseRank.objects.filter(semester=semester).values_list("student", flat=True)
        numFilled = len(set(filled))
        data = {
            "status": "success",
            "numFilled": numFilled,
            "numNotFilled": numUsers - numFilled,
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        return HttpResponseBadRequest()

# For Professor dashboard bar chart that shows how many Students are graduating, how many are in-progress, etc
def getStudentStats(request):
	semester = Semester.objects.get(is_active=True)
	numStudents = len(User.objects.filter(groups__name="Students"))
	data = {
        "status": "success",
        "graduated": 100,
        "rotating": 200,
        "newusers": 300,
    }
	return HttpResponse(json.dumps(data), content_type="application/json")