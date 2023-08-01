from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
# from .forms import ProfileForm
from .models import ProfileImages
from django.views.generic.edit import CreateView



class CreateProfileView(CreateView):
    model=ProfileImages
    success_url="/profiles"
    template_name="profiles/create_profile.html"
    fields = "__all__"




