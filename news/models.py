from email.policy import default
from django.db import models
# import tinymce editor 
from tinymce.models import HTMLField
# Autoslug import news models
from autoslug import AutoSlugField
# Create your models here.
# create a class
class News(models.Model):
    Title = models.CharField(max_length=150)
    Discription = HTMLField()
    # slug field create
    autoslug = AutoSlugField(populate_from=('Title'), unique=True, null=True, default=None)
