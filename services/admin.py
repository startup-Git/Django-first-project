from django.contrib import admin
from services.models import Services

# Register your models here.
# create a class
class ServiceAdmin(admin.ModelAdmin):
    ServicesDisplay = ('Icon','Title', 'Description')

admin.site.register(Services, ServiceAdmin)
