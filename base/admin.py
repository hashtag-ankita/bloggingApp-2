from django.contrib import admin
from .models import CustomUser, Category, Tag, Post

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
