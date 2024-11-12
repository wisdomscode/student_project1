from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
