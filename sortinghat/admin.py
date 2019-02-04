from django.contrib import admin
from .models import *

# Register your models here.
# Custom admin view for Hogwarts Semester
class SemesterAdmin(admin.ModelAdmin):
    def session_date(self, obj):
        return obj.start_date.strftime("%b %Y")
    list_display = ("session_date", "active")

# Custom admin view for Hogwarts House
class HouseAdmin(admin.ModelAdmin):
    def number_of_courses(self, obj):
        return len(Course.objects.filter(house=obj.id))
    list_display = ("house_name", "number_of_courses")
    ordering = ("house_name",)

# Custom admin view for Hogwarts Course
class CourseAdmin(admin.ModelAdmin):
    def professor_name(self, obj):
        return "%s %s" % (obj.professor.first_name, obj.professor.last_name) 
    list_display = ("course_name", "house", "active", "professor_name", "floor", "classroom")
    ordering = ("house", "course_name")

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

admin.site.register(Semester, SemesterAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(HouseRank, HouseRankAdmin)
admin.site.register(CourseRank, CourseRankAdmin)
admin.site.register(Match, MatchAdmin)