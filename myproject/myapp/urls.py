from django.urls import path
from . import views


urlpatterns = [
    path('fruits/',views.index,name="index")
    # path('add/',views.add,name="add")
]
