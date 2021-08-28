from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import  LoginView, LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    # Extra-Authentication
    # View Screen 
    path('pages-login', views.pages_login, name="pages-login"),
    path('pages-register', views.pages_register, name="pages-register"),
    path('recoverpw', views.pages_recoverpw, name="pages-recoverpw"),
    path('pages-lock-screen', views.pages_lock_screen, name="pages-lock-screen"),
    # View screen 2
    path('pages-login-2', views.pages_login_2, name="pages-login-2"),
    path('pages-register-2', views.pages_register_2, name="pages-register-2"),
    path('pages-recoverpw-2', views.pages_recoverpw_2, name="pages-recoverpw-2"),
    path('pages-lock-screen-2', views.pages_lock_screen_2, name="pages-lock-screen-2"),
    

]
