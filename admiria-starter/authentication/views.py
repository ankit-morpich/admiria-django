# from authentication.form import loginForms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.contrib.auth import SESSION_KEY, authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib.sessions.models import Session

# Login-1

username ='';

def pages_login(request):

    if 'username'  in request.session:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username =='':
                messages.info(request,'Please enter your username')
                return redirect('pages-login')
            elif password == '':
                messages.info(request,'Please enter your password')
                return redirect('pages-login')
            else:
                user = auth.authenticate(username=username, password=password)
                if user is not None:              
                    request.session['username'] = username
                    auth.login(request, user)
                    return redirect('dashboard')
                else:
                    messages.info(request, 'Invalid Credentials')
                    return redirect('pages-login')
        else:
            return render(request, 'pages/Extra/authentication/pages-login.html')

# Register-1

def pages_register(request):
    if 'username'  in request.session:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if username == '':
                messages.info(request,'username field is empty')
                return redirect('pages-register')
            elif email == '':
                messages.info(request,'email field is empty')
                return redirect('pages-register')
            elif password == '':
                messages.info(request,'password field is empty')
                return redirect('pages-register')
            else:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Is Allready Exists')
                    return redirect('pages-register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Is Allready Exists')
                    return redirect('pages-register')
                else:
                    send_mail(
                        'Welcome To Admiria',
                        'Congratulation for your membership.',
                        settings.EMAIL_HOST_USER,
                        [email],
                        fail_silently=False,
                    )
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('pages-login')
        else:
            return render(request, 'pages/Extra/authentication/pages-register.html')

# Recover Password-1

def pages_recoverpw(request):
    if request.method == "POST":
        email = request.POST['email']
        if email == '':
            messages.info(request,'Please Enter Your Email Address')
            return redirect ('pages-recoverpw')
        else:   
            if User.objects.filter(email=email).exists():
                # domain = request.headers['Host']
                password_reset_form = PasswordResetForm(request.POST)
                if password_reset_form.is_valid():
                    data = password_reset_form.cleaned_data['email']
                    associated_users = User.objects.filter(Q(email=data))

                    if associated_users.exists():
                        for user in associated_users:
                            subject = "Password Reset Requested"
                            email_template_name = "pages/Extra/authentication/email.txt"
                            c = {
                                "email": user.email,
                                'domain': '127.0.0.1:8000',
                                'site_name': 'website',
                                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                "user": user,
                                'token': default_token_generator.make_token(user),
                                'protocol': 'http',
                            }
                            email = render_to_string(email_template_name, c)
                            try:
                                send_mail(subject, email, 'admin@example.com',
                                        [user.email], fail_silently=False)
                            except BadHeaderError:
                                messages.info(request, "Email Doesn't Exists ")
                                return redirect('pages-recoverpw')
                            return redirect("password_reset_done")

                password_reset_form = PasswordResetForm()
                return render(request=request, template_name="pages/Extra/authentication/pages-recoverpw.html", context={"password_reset_form": password_reset_form})
            else:
                messages.info(request,"Email Address Doesn't Exist")
                return redirect('pages-recoverpw')
    else:
        return render(request, 'pages/Extra/authentication/pages-recoverpw.html')

# Lock Screen 1

def pages_lock_screen(request):
     
        if request.method == "POST":
            password = request.POST['password']
            user = auth.authenticate(uname=username,password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('pages-login')
        else:
            return render(request, 'pages/Extra/authentication/pages-lock-screen.html')

        

# Logout-1

def pages_logout(request):
    auth.logout(request)
    return render(request, 'pages/Extra/authentication/pages-logout.html')
    
# Login-2

def pages_login_2(request):
    if 'username'  in request.session:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username =='':
                messages.info(request,'Please enter your username')
                return redirect('pages-login-2')
            elif password == '':
                messages.info(request,'Please enter your password')
                return redirect('pages-login-2')
            else:
                user = auth.authenticate(username=username, password=password)
                if user is not None:              
                    request.session['username'] = username
                    auth.login(request, user)
                    return redirect('dashboard')
                else:
                    messages.info(request, 'Invalid Credentials')
                    return redirect('pages-login-2')
        else:
            return render(request, 'pages/Extra/authentication/pages-login-2.html')

# Register-2

def pages_register_2(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Is Allready Exists')
            return redirect('pages-register-2')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Is Allready Exists')
            return redirect('pages-register-2')
        else:
            send_mail(
                'Welcome To Admiria',
                'Congratulation for your membership.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()

            return redirect('pages-login-2')
    else:
        return render(request, 'pages/Extra/authentication/pages-register-2.html')

# Recover Password-2

def pages_recoverpw_2(request):

    if request.method == "POST":
        email = request.POST['email']
        if email == '':
            messages.info(request,'Please Enter Your Email Address')
            return redirect ('pages-recoverpw-2')
        else:
            if User.objects.filter(email=email).exists():
                password_reset_form = PasswordResetForm(request.POST)
                if password_reset_form.is_valid():
                    data = password_reset_form.cleaned_data['email']
                    associated_users = User.objects.filter(Q(email=data))

                    if associated_users.exists():
                        for user in associated_users:
                            subject = "Password Reset Requested"
                            email_template_name = "pages/Extra/authentication/email.txt"
                            c = {
                                "email": user.email,
                                'domain': '127.0.0.1:8000',
                                'site_name': 'website',
                                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                "user": user,
                                'token': default_token_generator.make_token(user),
                                'protocol': 'http',
                            }
                            email = render_to_string(email_template_name, c)
                            try:
                                send_mail(subject, email, 'admin@example.com',
                                        [user.email], fail_silently=False)
                            except BadHeaderError:
                                messages.info(request, "Email Doesn't Exists ")
                                return redirect('pages-recoverpw-2')
                            return redirect("password_reset_done")

                password_reset_form = PasswordResetForm()
                return render(request=request, template_name="pages/Extra/authentication/pages-recoverpw-2.html", context={"password_reset_form": password_reset_form})
            else:
                messages.info(request, "Email Does't Exist")
                return redirect('pages-recoverpw-2')
    else:
        return render(request, 'pages/Extra/authentication/pages-recoverpw-2.html')


# Lock Screen -2

def pages_lock_screen_2(request):
    return render(request, 'pages/Extra/authentication/pages-lock-screen-2.html')

# Logout-2

def pages_logout_2(request):
    auth.logout(request)
    return render(request, 'pages/Extra/authentication/pages-logout-2.html')

