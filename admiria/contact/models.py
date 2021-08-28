from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name 

    def __unicode__(self):
        return self.first_name
        
 