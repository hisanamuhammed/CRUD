from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length = 70)
    name = models.CharField(max_length = 70)
    email = models.EmailField(max_length = 70)
    password = models.CharField(max_length = 70)
    Confirm_password = models.CharField(max_length = 70)