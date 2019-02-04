from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# Hogwarts semester. Separate one needed for every "Sorting Hat" survey
class Semester(models.Model):
    start_date = models.DateField(default=datetime.date.today)
    active = models.BooleanField(default=True)
    def __str__(self):
        return "%s" % self.start_date.strftime("%Y %b")

# Hogwarts Houses - Gryffindor, Slytherin, Ravenclaw, Hufflepuff
class House(models.Model):
    house_name = models.CharField(max_length=200,unique=True,default="")
    def __str__(self):
        return self.house_name

# Hogwarts courses
class Course(models.Model):
    class Meta:
        unique_together = ("house", "course_name")
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=200)
    # Detailed description
    description = models.TextField(default="")
    # If a course is discontinued, don't delete it but change this field to False (for data purposes)
    active = models.BooleanField(default=True)
    floor = models.IntegerField(
        choices = ((x,x) for x in [1,2,3,4,5,6,7]),
        default=1,
    )
    classroom = models.CharField(max_length=30)
    professor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"groups__name": "Professors"})
    def __str__(self):
        return "[%s] %s" % (self.house.house_name, self.course_name)

# When the student submits the survey, the House rankings are stored here
class HouseRank(models.Model):
    class Meta:
        unique_together = ("student", "rank", "semester")
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"groups__name": "Students"})
    rank = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=Semester.objects.get(active=True).id)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    def __str__(self):
        return "%s #%d (%s)" % (self.student, self.rank, self.semester.start_date.strftime("%Y %b"))

# When the student submits the survey, the Course rankings are stored here
class CourseRank(models.Model):
    class Meta:
        unique_together = ("student", "rank", "semester")
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"groups__name": "Students"})
    rank = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=Semester.objects.get(active=True).id)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return "%s #%d (%s)" % (self.student, self.rank, self.semester.start_date.strftime("%Y %b"))

# After a survey is closed, the professors can run an algorithm to generate these objects
class Match(models.Model):
    # This allows the Admin control panel to display "Matches" instead of "Matchs" (which would be its default behaviour)
    class Meta:
        unique_together=("student","semester")
        verbose_name_plural = "matches"
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"groups__name": "Students"})
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=Semester.objects.get(active=True).id)
    def __str__(self):
        return "%s %s (%s)" % (self.student, self.course, self.semester.start_date.strftime("%Y %b"))