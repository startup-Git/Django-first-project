from django.contrib import admin
# import models class
from news.models import News

# Register your models here.
# create register models class

class NewsAdmin(admin.ModelAdmin): 
    NewsItems = ('Title','Discription')

# admin option create
admin.site.register(News, NewsAdmin)