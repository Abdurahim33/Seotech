from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from About.models import AboutModel

class AboutView(ListView):
    model = AboutModel
    template_name = 'about.html'