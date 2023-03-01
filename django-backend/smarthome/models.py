from django.db import models

# Create your models here.
class SmartHome(models.Model):
    plug = models.CharField(max_length=100)
