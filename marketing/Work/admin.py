from django.contrib import admin
from Work.models import Homepage_work, work_department

@admin.register(Homepage_work)
class Homepage_work_admin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ('title', 'sub_title')


@admin.register(work_department)
class Work_department_admin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'sub_title')
    list_display_links = ('icon', 'title', 'sub_title')