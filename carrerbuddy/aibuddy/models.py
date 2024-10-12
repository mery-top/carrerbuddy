from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    about = models.CharField(max_length=1000)
    interest = models.CharField(max_length=1000)
    wanted = models.CharField(max_length=1000)
    future = models.CharField(max_length=1000)