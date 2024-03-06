from django.contrib import admin
from Home.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'image')
    list_display_links = ('title', 'sub_title', 'image')

    