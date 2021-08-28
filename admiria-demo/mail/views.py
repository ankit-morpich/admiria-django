from django.shortcuts import render

# Create your views here.

def email_inbox(request):
    greeting = {}
    greeting['title'] = "Inbox"
    greeting['path'] = "Email"
    return render(request,'pages/Email/email-inbox.html',greeting)
def email_read(request):
    greeting = {}
    greeting['title'] = "Email Read"
    greeting['path'] = "Email"
    return render(request,'pages/Email/email-read.html',greeting)
def email_compose(request):
    greeting = {}
    greeting['title'] = "Email Compose"
    greeting['path'] = "Email"
    return render(request,'pages/Email/email-compose.html',greeting)