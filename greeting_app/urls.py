from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add-user', views.addUser, name='add_new_user'),
]