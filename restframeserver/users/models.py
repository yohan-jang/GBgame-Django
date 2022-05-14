from django.db import models
from argon2 import PasswordHasher


class Users(models.Model):
    mail = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=10)
    userid = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'users'

