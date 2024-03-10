from django.urls import path
from Work.views import Homepage_workview

app_name='Work'

urlpatterns = [
    path('Work/', Homepage_workview.as_view(), name='Work'),
]
