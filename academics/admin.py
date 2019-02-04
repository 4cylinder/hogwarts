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
    list_display = ("course_name", "year", "house", "active", "professor_name", "floor", "classroom")
    ordering = ("house", "course_name", "year")

admin.site.register(Semester, SemesterAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Course, CourseAdmin)