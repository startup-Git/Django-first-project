from django.contrib import admin

from contact.models import Contact
# Register your models here.
class AdminContactpannel(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'ContactNumber', 'Mails', 'Messages')

admin.site.register(Contact, AdminContactpannel)