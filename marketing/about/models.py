from django.db import models


class About(models.Model):
    image = models.ImageField(upload_to='aboutmodel/%Y/%m/%d')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'AboutModel'
        verbose_name_plural = 'AboutModels'