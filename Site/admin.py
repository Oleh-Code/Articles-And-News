from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_date', 'published_date', 'url','draft']
    list_editable = ['draft']
    list_display_links = ['title', 'created_date']