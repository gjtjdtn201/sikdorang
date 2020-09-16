from django.db import models
from django.conf import settings

class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    tags_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tags_user", blank=True)
    def __str__ (self):
        return self.name

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    Category_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__ (self):
        return self.name

class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20, null=True)
    tel = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(max_length=10, null=True)
    longitude = models.FloatField(max_length=10, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name = 'store_tags') 