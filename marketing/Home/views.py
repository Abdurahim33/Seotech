from django.shortcuts import render
from django.views.generic import ListView
from Home.models import Banner

class BannerView(ListView):
    model = Banner
    template_name = 'Home.html'