from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# model = 데이터가 보여지는 모습.

class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
