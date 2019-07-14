from django.contrib import admin
from . import models
from .models import Catagory
from .models import Tag
from .models import Blog
from .models import Comment
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','created')
    list_filter = ('created',)

admin.site.register(Blog,BlogAdmin)

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Catagory,CatagoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Tag,TagAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','content','blog','created')
    list_filter = ('created',)

admin.site.register(Comment,CommentAdmin)