from django.urls import path
from .import views

urlpatterns = [
    # Contect Us
    path('Contect_Us', views.contact_us, name='contect-us'),
]
