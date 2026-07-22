from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'tags')
    list_filter = ('date',)
    search_fields = ('titre', 'contenu')
