from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class Contact(models.Model):
    sno=AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=100)
