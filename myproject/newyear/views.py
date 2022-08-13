from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime




def index(request):
    now = datetime.now()
    print(now)
    print(now.day)
    print(now.month)

    return render(request,"newyear/newyear.html", 
    {
    'newyear':now.month == 1 and now.day == 1
    })
    

# Create your views here.
