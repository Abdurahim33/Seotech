from django.urls import path
from Team.views import Homepage_team_views

app_name='Team'

urlpatterns = [
    path('Team/',Homepage_team_views.as_view(), name='Team'),
]
