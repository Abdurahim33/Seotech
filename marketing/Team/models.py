from django.db import models
from Our_Service.abstract import BaseModel, OrderModel

class Homepage_Team(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Homepage_Team'
        verbose_name_plural = 'Homepage_Teams'

class Team(BaseModel, OrderModel):
    image = models.ImageField(upload_to='Team/%Y/%m/%d')
    name = models.CharField(max_length=50)
    about_the_worker = models.CharField(max_length=255)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

class Homepage_Testimonial(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Homepage_Testimonial'
        verbose_name_plural = 'Homepage_Testimonials'


class Testimonial(BaseModel, OrderModel):
    image = models.ImageField(upload_to='Testimonial/%Y/%m/%d')
    name = models.CharField(max_length=50)
    information = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
