'''Author: Fadhlan Ridhwanallah
   Date: 22 February 2019'''
   
from django.db import models

# Create your models here.
class ORMUser(models.Model):
    user_id = models.CharField(max_length=36, primary_key=True, null=False)
    handphone = models.CharField(max_length=13, null=False)
    password = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    created_at = models.DateField()
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

class ORMTaxObject(models.Model):
    TAX_CODE = (
        ('1', 'food'),
        ('2', 'tobacco'),
        ('3', 'entertainment'))

    tax_id = models.CharField(max_length=36, primary_key=True, null=False)
    user_id = models.ForeignKey(ORMUser, models.DO_NOTHING, db_column='user_id')
    tax_code = models.CharField(max_length=30, choices=TAX_CODE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_object'