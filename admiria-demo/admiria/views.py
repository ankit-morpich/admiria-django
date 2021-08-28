from django.shortcuts import render


# Create your views here.

## Main Home Page
def index(request):
    greeting = {}
    greeting['title'] = "Dashboard"
    greeting['path'] = "Dashboard"
    return render(request,'pages/index.html',greeting)
# Dashboard 2
def dashboard(request):
    greeting = {}
    greeting['title'] = "Dashboard 2"
    greeting['path'] = "Dashboard"
    return render(request,'pages/dashboard.html',greeting)
# Widgets
def widget(request):
    greeting = {}
    greeting['title'] = "Widgets"
    greeting['path'] = "Main"
    return render(request,'pages/widgets.html',greeting)
# Calender
def calendar(request):
    greeting = {}
    greeting['title'] = "Calendar"
    greeting['path'] = "Main"
    return render(request,'pages/calendar.html',greeting)
# Help & Support
def faq(request):
    greeting = {}
    greeting['title'] = "FAQ"
    greeting['path'] = "Main"
    return render(request,'pages/faq.html',greeting)


