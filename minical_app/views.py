from django.shortcuts import render

# Create your views here.

def summation(request):
    return render(request, 'cal_temp/calculator.html')
