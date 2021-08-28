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
    path('logout', views.pages_logout, name="pages-logout"),
    path('recoverpw', views.pages_recoverpw, name="pages-recoverpw"),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='pages/Extra/authentication/pages-changepw-form.html'),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='pages/Extra/authentication/pages-changepw-done.html'),name='password_change_done'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='pages/Extra/authentication/pages-resetpw.html') ,name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='pages/Extra/authentication/pages-changepw.html') ,name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='pages/Extra/authentication/pages-resetpwcomplate.html') ,name='password_reset_complete'),
    path('pages-lock-screen', views.pages_lock_screen, name="pages-lock-screen"),
    path('logout',auth_views.LogoutView.as_view(template_name='pages/Extra/authentication/pages-logout.html'),name='logout'),
    # View screen 2
    path('pages-login-2', views.pages_login_2, name="pages-login-2"),
    path('pages-register-2', views.pages_register_2, name="pages-register-2"),
    # path('logout', views.pages_logout_2, name="pages-logout-2"),
    path('pages-recoverpw-2', views.pages_recoverpw_2, name="pages-recoverpw-2"),
    # path('password_change/',auth_views.PasswordChangeView.as_view(template_name='pages/Extra/authentication/pages-changepw-form-2.html'),name='password_change'),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='pages/Extra/authentication/pages-changepw-done-2.html'),name='password_change_done'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='pages/Extra/authentication/pages-resetpw-2.html') ,name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='pages/Extra/authentication/pages-changepw-2.html') ,name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='pages/Extra/authentication/pages-resetpwcomplate-2.html') ,name='password_reset_complete'),
    path('pages-lock-screen-2', views.pages_lock_screen_2, name="pages-lock-screen-2"),
    

]
