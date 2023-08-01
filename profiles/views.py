from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
# from .forms import ProfileForm
from .models import ProfileImages
from django.views.generic.edit import CreateView
from django.views.generic import ListView



class CreateProfileView(CreateView):
    model=ProfileImages
    success_url="/profiles"
    template_name="profiles/create_profile.html"
    fields = "__all__"


class ProfileListView(ListView):
    model = ProfileImages
    template_name="profiles/user_profiles.html"
    context_object_name = "profiles"





