from django.shortcuts import redirect, render

# Login-1

username ='';

def pages_login(request):
    return render(request, 'pages/Extra/authentication/pages-login.html')

# Register-1

def pages_register(request):
    return render(request, 'pages/Extra/authentication/pages-register.html')

# Recover Password-1

def pages_recoverpw(request):
    return render(request, 'pages/Extra/authentication/pages-recoverpw.html')

# Lock Screen 1

def pages_lock_screen(request):
    return render(request, 'pages/Extra/authentication/pages-lock-screen.html')

        
# Login-2

def pages_login_2(request):
    return render(request, 'pages/Extra/authentication/pages-login-2.html')

# Register-2

def pages_register_2(request):
    return render(request, 'pages/Extra/authentication/pages-register-2.html')

# Recover Password-2

def pages_recoverpw_2(request):
    return render(request, 'pages/Extra/authentication/pages-recoverpw-2.html')


# Lock Screen -2

def pages_lock_screen_2(request):
    return render(request, 'pages/Extra/authentication/pages-lock-screen-2.html')

