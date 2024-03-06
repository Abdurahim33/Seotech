from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Banner/%Y/%m/%d')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    