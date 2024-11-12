from django.shortcuts import render
from  .models import Student
# Create your views here.

def homepage(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})


def createStudent(request):
    return render(request, 'students/create_student.html')
