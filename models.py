from django.db import models


class Student(models.Model):
    StudentName=models.CharField(max_length=255)
    RegNo=models.CharField(max_length=25)
    AcademicYear=models.CharField(max_length=25)
    Semester=models.IntegerField()
    Code=models.CharField(max_length=25)
    Title=models.CharField(max_length=255)
    Cat=models.IntegerField()
    Exam=models.IntegerField()
    Total=models.IntegerField()
    Grade=models.CharField(max_length=2)
    Recommendation=models.CharField(max_length=255)

