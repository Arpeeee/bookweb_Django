from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")

def view_home(request):
    from datetime import datetime
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })