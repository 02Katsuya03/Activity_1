from django.shortcuts import render
from django.views.generic import TemplateView

class BasePageView(TemplateView):
    template_name = 'app/base.html'

class HomePageView(TemplateView):
    template_name = 'app/Home.html'

class AboutPageView(TemplateView):
    template_name = 'app/About.html'

