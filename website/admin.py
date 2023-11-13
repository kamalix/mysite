from django.contrib import admin
from website.models import Contact,Newsletter

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name','email','subject','created_date']
    search_fields = ['subject','message','name']
    list_filter = ['email']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)
