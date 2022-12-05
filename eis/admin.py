from django.contrib import admin

from eis.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "time_created")
    search_fields = ("title", )
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Article, ArticleAdmin)
