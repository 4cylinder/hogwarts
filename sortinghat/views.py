# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import *
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
import json, mimetypes, os
from surveyform import *

# Create your views here.

# Survey question page for Students
@login_required
def student_survey(request):
	houses = House.objects.all()
	courses = Course.objects.filter(active=True)
	activesemester = Semester.objects.get(active=True)
	# Format the date so it can be displayed on the actual template
    activesemester.start_date = activesemester.start_date.strftime("%b %Y")
    # Check whether or not the Student has already answered the survey
    firstTime = len(HouseRank.objects.filter(student=request.user,semester=activesemester))==0

    return render(request, "survey/student_survey.html", context={
        "form": TRACKerForm(firstTime=firstTime,student=request.user,semester=activesemester),
        "firstTime": firstTime,
        "semester": activesemester,
    })

# Survey submission and processing for Students
@login_required
def student_submit(request):
	activesemester = Semester.objects.get(active=True)
	# Get ranking of Houses
	# Get ranking of Courses
	return

# Survey question page for Professors
@login_required
def professor_survey(request):
	if request.user.is_staff:
        activesemester = Semester.objects.get(active=True)
        return render(request, "survey/manager_survey.html", context={
        })
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")

# Survey submission and processing for Professors
@login_required
def professor_submit(request):
	activesemester = Semester.objects.get(active=True)
	return

