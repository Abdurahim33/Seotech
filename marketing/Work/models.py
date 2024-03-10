from django.db import models
from Our_Service.abstract import OrderModel

class Homepage_work(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Homepage_work'
        verbose_name_plural = 'Homepage_works'



class work_department(OrderModel):
    icon = models.ImageField(upload_to='work_department/%Y/%m/%d')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Work_department'
        verbose_name_plural = 'Work_departments'