from django.contrib import admin

from eis.models import Article, Additional, URLs


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


class URLAdmin(admin.ModelAdmin):
    list_display = ("url", )
    search_fields = ("url", )


admin.site.register(URLs, URLAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Additional, AdditionalAdmin)
