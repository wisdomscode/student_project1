from django.shortcuts import render
from django.http import HttpResponse



# def index(request):
#     return HttpResponse('<h1>Hello, world</h1>')


def index(request):
    name = 'Ahmed'
    age = 23
    friends = ['James', 'Tom', 'Ann', 'Juliet']
    gender = 'female'
    context = {
        'name': name, 
        'age': age, 
        'friends': friends,
        'gender': gender
     }
    return render(request, 'index.html', context=context)

def addUser(request):
    return render(request, 'add_user.html')