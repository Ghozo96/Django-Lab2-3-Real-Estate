from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'state', 'zipcode', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('title',)
    list_filter = ('realtor',)
    search_fields = ('title', 'state',)
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)
