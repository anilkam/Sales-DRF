# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username', unique=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Admin'


class Cart(models.Model):
    userid = models.AutoField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cart'


class Category(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class Orderdetail(models.Model):
    orderheaderid = models.IntegerField(db_column='OrderHeaderID', blank=True, null=True)  # Field name made lowercase.
    productid = models.AutoField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderDetail'


class Orderheader(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    itemtotal = models.FloatField(db_column='ItemTotal', blank=True, null=True)  # Field name made lowercase.
    discountapplied = models.FloatField(db_column='DiscountApplied', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.IntegerField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderHeader'


class Product(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class User(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username', unique=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
