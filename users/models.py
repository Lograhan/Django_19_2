from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=35, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Почта')
    u_image = models.ImageField(upload_to='users/', verbose_name='Аватар', null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='Страна')
    email_verify = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
