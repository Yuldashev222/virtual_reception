from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='Admin/images/', blank=True, validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg", "svg"])])
    info = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.username