from django.shortcuts import render
items = ['apple', 'banana', 'orange']
# Create your views here.
def index(request):
  return render(request,'task/index.html',{
    'items' : items
  })
