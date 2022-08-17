from django.shortcuts import render
items = ['Some', 'Random', 'Items']
def index(request):
    return render(request, 'lstapp/index.html', {
        'items':items
    })
