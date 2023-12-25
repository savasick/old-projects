from django.contrib import admin
from .models import Author, Book, Language


admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Author)

