from django.urls import path
from . import views


app_name = 'myapps'

urlpatterns = [
    path('fruits/',views.index,name="index"),
    path('add',views.add, name="add"),
    path('task',views.task,name="task"),
]
