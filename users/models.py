from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# model = 데이터가 보여지는 모습.

class User(AbstractUser):

    bio = models.TextField(default="")
