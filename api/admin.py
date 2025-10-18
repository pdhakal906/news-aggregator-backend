from django.contrib import admin
from .models import News, Me


admin.site.register(Me)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "source", "created_at")
    list_filter = ("source",)
