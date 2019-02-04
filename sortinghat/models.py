from django.db import models
from django.contrib.auth.models import User
import datetime
from academics.models import *

# Create your models here.
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