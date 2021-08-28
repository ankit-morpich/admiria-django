from django.contrib import admin
from django.db.models.base import Model
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__','email','subject','message']
    class Meta:
        model = Contact




admin.site.register(Contact)
