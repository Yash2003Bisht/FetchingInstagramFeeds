from django.db import models

# Create your models here.
class Data(models.Model):
    link = models.CharField(max_length=500, unique=True)
    timestamp = models.CharField(max_length=500)