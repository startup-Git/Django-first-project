from django.db import models

# Create your models here.

# create class models
class Services(models.Model):
    Icon = models.CharField(max_length=60)
    Title = models.CharField(max_length=60)
    Description = models.TextField()