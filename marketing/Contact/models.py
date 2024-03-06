from django.db import models

class Contact_Model(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=255)