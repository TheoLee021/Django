from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False, blank=True)
    last_name = models.CharField(max_length=150, editable=False, blank=True)
    name = models.CharField(max_length=150, blank=True)
    is_host = models.BooleanField(default=False)