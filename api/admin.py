from django.contrib import admin

from api.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author")


admin.site.register(Article, ArticleAdmin)
