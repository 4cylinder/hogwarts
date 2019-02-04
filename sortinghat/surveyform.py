from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django import forms
from django_select2.forms import Select2Widget, Select2MultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field
from .models import *

class StudentSurveyForm(forms.Form):
    
    def __init__(self, firstTime=True,student=None, semester=None, *args, **kwargs):
        super(StudentSurveyForm, self).__init__(*args, **kwargs)

class ProfessorSurveyForm(forms.Form):

    def __init__(self, firstTime=True,professor=None, semester=None, *args, **kwargs):
        super(ProfessorSurveyForm, self).__init__(*args, **kwargs)