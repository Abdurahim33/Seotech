from django.contrib import admin
from Team.models import Homepage_Team, Team, Homepage_Testimonial, Testimonial

@admin.register(Homepage_Team)
class Homepage_Team_admin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ('title', 'sub_title')

@admin.register(Team)
class Team_admin(admin.ModelAdmin):
    list_display = ('image', 'name', 'about_the_worker', 'facebook_link', 'twitter_link', 'linkedin_link', 'instagram_link')
    list_display_links = ('image', 'name', 'about_the_worker', 'facebook_link', 'twitter_link', 'linkedin_link', 'instagram_link')


@admin.register(Homepage_Testimonial)
class Homepage_Testimonials_admin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ('title', 'sub_title')



@admin.register(Testimonial)
class Testimonial_admin(admin.ModelAdmin):
    list_display = ('image', 'name', 'information')
    list_display_links = ('image', 'name', 'information')