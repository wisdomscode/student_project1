from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-user', views.addUser, name='add_new_user'),
    path('show-name', views.showName, name='show_name'),
]