from django.contrib import admin
from .models import Column, Article


# Register your models here.
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'infro')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')


admin.register(Column, ColumnAdmin)
admin.register(Article, ArticleAdmin)
