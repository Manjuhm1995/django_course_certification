from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
# class CreateProfileView(TemplateView):
#     template_name = "profiles/create_profile.html"
class CreateProfileView(View):
    def get(self,request):
        return render(request,"profiles/create_profile.html")
    def post(self,request):
        image_file=request.FILES["image"]
        print(image_file)
        # store_file(image_file)
        return HttpResponseRedirect("/profiles")
# def store_file(file):
#     with open("tmp/image.jpg","wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


