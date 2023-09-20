from django.db import models

# Create your models here.
class Kino(models.Model):
    country = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    year = models.IntegerField()