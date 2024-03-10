from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from Our_Service.models import Homepage, department

class HomepageView(ListView):
    template_name = 'service.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = Homepage.objects.all()
        return qs
    

    def get_context_data(self, **kwargs: Any):
        data = super().get_context_data(**kwargs)
        data['department'] = department.objects.all()
        return data