from pyexpat import model
from django.db import models
#from django.contrib.auth.models import User


class Usuario(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
