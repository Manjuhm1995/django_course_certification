from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .forms import ReviewForm
from .models import Review
# Create your views here.

class Reviews(View):
  def get(self,request):
    form = ReviewForm()
    return render(request, "reviews/review.html", {
      "form": form
    })

  def post(self,request):
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/thank-you")
    return render(request, "reviews/review.html", {
      "form": form
    })

class ReviewListView(TemplateView):
  template_name = "reviews/review_list.html"
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    review=Review.objects.all()
    context["reviews"]=review
    return context
class ThankYou(TemplateView):
  template_name = "reviews/thank_you.html"
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context["message"]="thi is working"
    return context