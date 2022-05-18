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
    user_num = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'users'


class Shop(models.Model):
    product_num = models.IntegerField(primary_key=True)
    product_type = models.CharField(max_length=20, blank=True, null=True)
    product_name = models.CharField(max_length=20, blank=True, null=True)
    product_price = models.IntegerField(blank=True, null=True)
    product_detail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'


class Rank(models.Model):
    mail = models.CharField(primary_key=True, max_length=20)
    tier = models.CharField(max_length=10, blank=True, null=True)
    rankpoint = models.IntegerField(blank=True, null=True)
    user_num = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank'


class Order(models.Model):
    order_num = models.IntegerField(primary_key=True)
    user_num = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    orderdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class JoinRecord(models.Model):
    idx = models.AutoField(primary_key=True)
    user_num = models.IntegerField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'join_record'


class GameRecord(models.Model):
    user_num1 = models.IntegerField(primary_key=True)
    user_num2 = models.IntegerField()
    user_num3 = models.IntegerField()
    user_num4 = models.IntegerField()
    user_num5 = models.IntegerField()
    user_num6 = models.IntegerField()
    start_date = models.DateTimeField(blank=True, null=True)
    avg_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_record'
        unique_together = (('user_num1', 'user_num2', 'user_num3', 'user_num4', 'user_num5', 'user_num6'),)


class ClassChart(models.Model):
    class_name = models.CharField(primary_key=True, max_length=10)
    max_point = models.IntegerField(blank=True, null=True)
    min_point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_chart'


class Changeinfo(models.Model):
    change_num = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=20, blank=True, null=True)
    prior_rank = models.CharField(max_length=10, blank=True, null=True)
    next_rank = models.CharField(max_length=10, blank=True, null=True)
    prior_money = models.IntegerField(blank=True, null=True)
    next_money = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    avg_rank = models.IntegerField(blank=True, null=True)
    user_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changeinfo'


class ChangeRecord(models.Model):
    change_num = models.IntegerField(primary_key=True)
    user_num = models.IntegerField(blank=True, null=True)
    cash_amount = models.IntegerField(blank=True, null=True)
    change_type = models.CharField(max_length=45, blank=True, null=True)
    change_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_record'


class Asset(models.Model):
    mail = models.CharField(primary_key=True, max_length=20)
    cash = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    user_num = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset'


