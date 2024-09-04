from django.contrib import admin
from .models import Book

# Register your models here.
# generic site of admin book
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'price']
    list_filter = ['published']
    search_fields = ['title']


