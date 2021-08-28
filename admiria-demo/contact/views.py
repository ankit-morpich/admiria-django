from django.contrib import messages
from django.shortcuts import redirect, render
from contact.models import Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# Contect Us
def contact_us(request):
    greeting = {}
    greeting['title'] = "Contact Us"
    greeting['path'] = "Main"
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name,email,subject,message)
        if name == '':
            messages.info(request,"name field Is empty")
            return redirect('contect-us')
        elif email == '':
            messages.info(request,"Email field Is empty")
            return redirect('contect-us')
        elif subject == '':
            messages.info(request,"Subject field Is empty")
            return redirect('contect-us')
        elif message == '':
            messages.info(request,'Please enter your message')
            return redirect('contect-us')
        else:
            send_mail(
               'Thank you Connect with Admiria',
               'Thank You for Contect Us will connect to you ',
               settings.EMAIL_HOST_USER,
               [email],
               fail_silently=False,
            )
            reg = Contact(first_name=name,email=email,subject=subject,message=message)
            reg.save()            
            return redirect ('/')
    else:
        return render(request,'pages/contact.html',greeting)