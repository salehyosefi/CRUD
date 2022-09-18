from django.contrib import admin
from .models import Book

class AdminMode(admin.ModelAdmin):
    list_display = ['name', 'store_name', 'fav']
    search_fields = ['name', 'store_name']

admin.site.register(Book, AdminMode)
