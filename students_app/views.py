from django.shortcuts import redirect, render
from  .models import Student
from django.contrib import messages


def homepage(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})


def createStudent(request):
    if request.method == 'POST':
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        department = request.POST.get('department')

        # check if all field are provided
        if not all([firstName, lastName, age, gender, department]) :
            messages.error(request, 'All fields are required')
            return render(request, 'students/create_student.html')


        try: 
            # create the Student instance
            Student.objects.create(
                first_name=firstName, 
                last_name=lastName,
                age=age, 
                gender=gender, 
                department=department
            )
            return redirect('home_page')  # redirect to home page using name in url
        
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'students/create_student.html')

    return render(request, 'students/create_student.html')


def showStudent(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'students/show_student.html', {'student': student})


def editStudent(request, id):
    student = Student.objects.get(id=id)

    # to update the student
    if request.method == 'POST':
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        department = request.POST.get('department')

        # check if all field are provided
        if not all([firstName, lastName, age, gender, department]) :
            messages.error(request, 'All fields are required')
            return render(request, 'students/edit_student.html')
        
        student.first_name = firstName
        student.last_name = lastName
        student.age = age
        student.gender = gender
        student.department = department

        student.save()
        return redirect('showStudentDetails', student.id)


    return render(request, 'students/edit_student.html', {'student': student})


def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('home_page')

    return render(request, 'students/delete_student.html', {'student': student})
