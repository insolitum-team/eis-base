from django.contrib import admin

from eis.models import Article, Additional


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "time_created")
    search_fields = ("title", )
    list_filter = ("time_created", )
    prepopulated_fields = {"slug": ("title", )}


class AdditionalAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "time_created")
    search_fields = ("title", )
    list_filter = ("time_created", )
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Additional, AdditionalAdmin)
