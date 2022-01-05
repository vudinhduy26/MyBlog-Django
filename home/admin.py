from django.contrib import admin
from .models import *

# Register your models here.

class Content_home(admin.ModelAdmin):
    list_display = ('id','title','datetime','author')
    #list_filter = ('title','datetime')
    #
    prepopulated_fields = {'slug': ('title',)}

class categories(admin.ModelAdmin):
    list_display = ('id','name')
    #tu dong dien duong dan giong ten tieu de danh muc
    prepopulated_fields = {'slug': ('name',)}

class child_cates(admin.ModelAdmin):
    list_display = ('id','name')
    #tu dong dien duong dan giong ten tieu de danh muc
    prepopulated_fields = {'slug_child': ('name',)}

admin.site.register(content_home,Content_home)
admin.site.register(categorie,categories)
admin.site.register(child_cate,child_cates)