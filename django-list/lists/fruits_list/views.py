from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

items=["Apple","Banana","Orange"]
def index(request):
    return render(request,"fruits_list/index.html",{
        'items':items
    })