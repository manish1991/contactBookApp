from django.contrib import admin
from contacts.models import Contact

# Register your models here.
class AdminContacts(admin.ModelAdmin):
    list_display = ('firstName', 'lastName','email','phone_number','created_by')
    search_fields = ('firstName','email')


admin.site.register(Contact, AdminContacts)
