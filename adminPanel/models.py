from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='Admin/images/', blank=True)
    info = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.username