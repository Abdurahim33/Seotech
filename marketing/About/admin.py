from django.contrib import admin
from About.models import AboutModel

@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'sub_title')
    list_display_links = ('image', 'title', 'sub_title')
    