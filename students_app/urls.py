from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('create', views.createStudent, name='createStudent'),
    path('show/<int:id>', views.showStudent, name='showStudentDetails'),
    path('edit/<int:id>', views.editStudent, name='editStudent'),
    path('delete/<int:id>', views.deleteStudent, name='deleteStudent'),
]