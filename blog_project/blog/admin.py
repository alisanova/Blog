from django.contrib import admin
from .models import Post, Category

admin.site.register((Post, Category))