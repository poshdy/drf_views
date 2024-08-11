from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField(max_length=200)
