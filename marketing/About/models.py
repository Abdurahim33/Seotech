from django.db import models
from About.abstract import BaseModel


class AboutModel(BaseModel):
    image = models.ImageField(upload_to='AboutModel/%Y/%m/%d', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    sub_title = models.TextField( null=True, blank=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'AboutModel'
        verbose_name_plural = 'AboutModels'