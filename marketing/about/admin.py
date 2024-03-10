from django.contrib import admin
from about.models import About

@admin.register(About)
class Aboutadmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'sub_title')
    list_display_links = ('image', 'title', 'sub_title')