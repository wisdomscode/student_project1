from django.shortcuts import render
from django.http import HttpResponse



# def index(request):
#     return HttpResponse('<h1>Hello, world</h1>')


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        # print(name, age, gender)

        friends = ['James', 'Tom', 'Ann', 'Juliet']
        context = {
            'name': name, 
            'age': age, 
            'friends': friends,
            'gender': gender
        }
        return render(request, 'greetings/index.html', context=context)
    return render(request, 'greetings/index.html')

def addUser(request):
    return render(request, 'greetings/add_user.html')


def showName(request):
    my_name = request.GET.get('name')
    return render(request, 'greetings/show_my_name.html', {'my_name': my_name})