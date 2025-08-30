from django.contrib import admin

from core.models import IndexPage


@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "image")
    search_fields = ("name",)
    list_filter = ("name",)
