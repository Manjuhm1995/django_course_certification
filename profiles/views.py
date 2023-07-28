from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import ProfileImages



class CreateProfileView(View):
    def get(self,request):
        form=ProfileForm()
        return render(request,"profiles/create_profile.html",{"form":form})
    def post(self,request):
        submitted_form=ProfileForm(request.POST,request.FILES)
        if submitted_form.is_valid():
            image_file=request.FILES["user_image"]
            image_path=ProfileImages(image=image_file)
            image_path.save()
            return HttpResponseRedirect("/profiles")
        return render(request,"profiles/create_profile.html",{"form":submitted_form})




