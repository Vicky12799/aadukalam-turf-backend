# Create your models here.
from django.db import models

class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    secondary_phone_number = models.CharField(max_length=15, blank=True, null=True)
    mail_id = models.EmailField()


    def __str__(self):
        return self.name
