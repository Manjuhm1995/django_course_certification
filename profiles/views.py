from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm


def store_file(file):
    with open("tmp/image.jpg","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
# class CreateProfileView(TemplateView):
#     template_name = "profiles/create_profile.html"
class CreateProfileView(View):
    def get(self,request):
        form=ProfileForm()
        return render(request,"profiles/create_profile.html",{"form":form})
    def post(self,request):
        submitted_form=ProfileForm(request.POST,request.FILES)
        if submitted_form.is_valid():
            image_file=request.FILES["image"]
            # print(image_file)
            store_file(image_file)
            return HttpResponseRedirect("/profiles")
        return render(request,"profiles/create_profile.html",{"form":submitted_form})




