from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    cost = models.IntegerField()
    description = models.CharField(max_length=255)
    pushed_product = models.CharField(max_length=50)
    callback = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
