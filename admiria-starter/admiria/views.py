from django.shortcuts import render


# Create your views here.

## Main Home Page
def index(request):
    greeting = {}
    greeting['title'] = "Dashboard"
    greeting['path'] = "Dashboard"
    return render(request,'pages/starter.html',greeting)
