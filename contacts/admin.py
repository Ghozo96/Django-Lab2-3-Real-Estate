from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'name', 'message', 'email', 'phone', 'contact_date')
    list_display_links = ('name', 'message')
    list_filter = ('listing',)
    search_fields = ('listing', 'name', 'message', 'email', 'phone')
    list_per_page = 25
    
admin.site.register(Contact, ContactAdmin)
