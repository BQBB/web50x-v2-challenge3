from django.shortcuts import render
from django.http import HttpResponse
from django.forms import forms

class Tsaks(forms.Form):
    taskname = forms


items = ['Banana' , 'Avocado' , 'Orange']

def index(request):
    return render(request,"myapp/fruits.html" ,{'items':items})



# def add(requset):
#     if requset.method == 'POST'
#         taskName

#         return render(requset, "myapp/add.html")

        


    


# Create your views here.
