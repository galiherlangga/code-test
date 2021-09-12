from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_number   = models.CharField(unique=True, max_length=20)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.EmailField(max_length=50, unique=True, error_messages={'unique':"Email sudah digunakan"})
    date_of_birth   = models.DateField(null=True, blank=True)
    gender          = models.CharField(max_length=10, blank=True, null=True)
