from django.db import models
from About.abstract import BaseModel, OrderModel

class Homepage(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Homepage'
        verbose_name_plural = 'Homepages'


class department(BaseModel, OrderModel):
    image = models.ImageField(upload_to='department/%Y/%m/%d')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'department'
