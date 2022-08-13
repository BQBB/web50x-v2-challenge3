from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


class TaskForm(forms.Form):
    task_name = forms.CharField(label='New Task  ', max_length=25, min_length=2)



items = ['Banana' , 'Avocado' , 'Orange']
def index(request):
    return render(request,"myapp/fruits.html" ,{'items':items})


# tasks = ['Task 1', 'Task 2', 'Task 3']
def task(request):
    if 'tasks' not  in request.session:
        request.session['tasks'] = []
    return render(request, 'myapp/task.html' ,{'tasks':request.session['tasks']})



def add(request):
    if request.method == 'GET':
        return render(request, 'myapp/add.html', {'form':TaskForm()} )


    if request.method == 'POST':
        formdata = TaskForm(request.POST)
        if formdata.is_valid():
            taskName = formdata.cleaned_data['task_name']
            request.session['tasks'] += [taskName]
            return HttpResponseRedirect(reverse('myapps:task'))
        else:
            return render(request, 'myapp/add.html' , {'formdata':formdata})

        


    


# Create your views here.
