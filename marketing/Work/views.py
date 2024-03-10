from django.shortcuts import render
from typing import Any
from django.views.generic import ListView
from Work.models import Homepage_work, work_department
from django.db.models.query import QuerySet

class Homepage_workview(ListView):
    template_name = 'work.html'


    def get_queryset(self) -> QuerySet[Any]:
      qs = Homepage_work.objects.all()
      return qs
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
         data = super().get_context_data()
         data['departments'] = work_department.objects.all()
         return data


