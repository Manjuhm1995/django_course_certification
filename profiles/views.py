from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
class CreateProfileView(TemplateView):
    template_name = "profiles/create_profile.html"
