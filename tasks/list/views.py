from django.shortcuts import render

# Create your views here.


items = ['Python','Php', 'JavaScript', 'Java', 'C#','Go']
def index(request):
    return render(request, 'list/index.html', {
        'items' : items
    })