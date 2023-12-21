from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'index.html'

class aboutUs(TemplateView):
    template_name = 'about-us.html'
    
class contactUs(TemplateView):
    template_name = 'contact-us.html'