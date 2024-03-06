from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True

class OrderModel(models.Model):
    order =models.IntegerField(verbose_name='order')


    class Meta:
        abstract = True