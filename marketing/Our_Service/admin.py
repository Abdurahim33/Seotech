from django.contrib import admin
from Our_Service.models import Homepage, department

@admin.register(Homepage)
class Homepage_Admin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ('title', 'sub_title')


@admin.register(department)
class department_admin(admin.ModelAdmin):
    list_display = ('image', 'title', 'sub_title')
    list_display_links = ('image', 'title', 'sub_title')


    
