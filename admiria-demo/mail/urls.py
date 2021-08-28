from django.urls import path, include
from . import views

urlpatterns = [

    # Email
    path('email-inbox', views.email_inbox, name="email-inbox"),
    path('email-read', views.email_read, name="email-read"),
    path('email-compose', views.email_compose, name="email-compose"),
]