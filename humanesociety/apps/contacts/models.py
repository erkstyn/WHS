from django.db import models

class Contact(models.Model):

    hours = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField(max_length=75, null=True, blank=True)
