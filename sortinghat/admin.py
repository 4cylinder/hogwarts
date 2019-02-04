from django.contrib import admin
from academics.models import *
from .models import *

# Register your models here.
# Custom admin view for House Rankings (from survey)
class HouseRankAdmin(admin.ModelAdmin):
    def student_name(self, obj):
        return "%s %s" % (obj.student.first_name, obj.student.last_name) 
    list_display = ("semester", "student_name", "rank", "house")
    ordering=("semester","rank")

# Custom admin view for Course Rankings (from survey)
class CourseRankAdmin(admin.ModelAdmin):
    def student_name(self, obj):
        return "%s %s" % (obj.student.first_name, obj.student.last_name)
    def course_name(self, obj):
        return obj.course.course_name
    def course_house(self, obj):
        return obj.house.house_name
    list_display = ("semester", "student_name", "rank","course_name", "course_house")
    ordering=("semester","rank")

# Custom admin view for Survey Matches
class MatchAdmin(admin.ModelAdmin):
    def student_name(self, obj):
        return "%s %s" % (obj.student.first_name, obj.student.last_name) 
    def professor_name(self, obj):
        return "%s %s" % (obj.professor.first_name, obj.professor.last_name)
    def course_name(self, obj):
        return obj.course.course_name
    def course_house(self, obj):
        return obj.house.house_name
    list_display = ("semester", "student_name", "course_name", "course_house", "professor_name")

admin.site.register(HouseRank, HouseRankAdmin)
admin.site.register(CourseRank, CourseRankAdmin)
admin.site.register(Match, MatchAdmin)