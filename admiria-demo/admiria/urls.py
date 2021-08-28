"""admiria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import urls
from django.contrib import admin
from django.urls import path,include
from .import  views

admin.site.site_header="Admiria"
admin.site.site_title = "Admin | Admiria"
admin.site.index_title = "Welcome to Admiria's Admin"
urlpatterns = [
    
    # Main Home Page
    path('', views.index, name="dashboard"),
    
    # Dashboard 2
    path('dashboard', views.dashboard, name='dashboard-1'),
    
    # Widgets
    path('widgets', views.widget, name="widget"),
    
    # Calender
    path('calendar', views.calendar, name="calendar"),

    # Help & Support
    path('faq', views.faq, name="faq"),

    # Contect Us
    path('',include('contact.urls')),
    
    # Admin 
    path('admin/', admin.site.urls),
    
    # Link Components
    path('Components/',include('components.urls')),
    
    # Link Anothers APP
    path('Extra/',include('extra.urls')),
    
    # Link Ecommerce
    path('Ecommerce/',include('ecommerce.urls')),
    
    # Link Email 
    path('Email/',include('mail.urls')),
    
    # Link Account Authentication
    path('authentication/',include('authentication.urls')),
    
    # Social Media Links
    path('authentication/', include('django.contrib.auth.urls')),


]