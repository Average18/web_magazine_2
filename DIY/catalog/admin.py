from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created']


@admin.register(models.Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']


@admin.register(models.Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'product']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)

