from django.urls import path
from Our_Service.views import HomepageView

app_name='Service'

urlpatterns = [
    path('Service/', HomepageView.as_view(), name='Service'),
]
