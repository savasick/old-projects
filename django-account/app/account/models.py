from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

class Account(AbstractUser):
    avatar = models.ImageField(upload_to='account/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=["jpeg", "jpg", "png"])])
    bio = models.TextField(max_length=500, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
