from django.urls import path
from About.views import AboutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)