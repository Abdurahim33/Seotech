from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from Team.models import Homepage_Team, Team, Homepage_Testimonial, Testimonial

class Homepage_team_views(ListView):
    template_name = 'Team.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = Homepage_Team.objects.all()
        return qs
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data= super().get_context_data(**kwargs)
        data['Team'] = Team.objects.all()
        data['homepage_testimonials'] = Homepage_Testimonial.objects.all()
        data['Testimonial'] = Testimonial.objects.all()
        return data
