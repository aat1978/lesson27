from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
