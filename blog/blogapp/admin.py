from django.contrib import admin

# Register your models here.
# используется для того чтобы модели подключить к админке

from .models import Category, Post, Tag

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)