from django.urls import path
from Home.views import BannerView

app_name='Home'

urlpatterns = [
    path('', BannerView.as_view(), name='Banner'),
]
