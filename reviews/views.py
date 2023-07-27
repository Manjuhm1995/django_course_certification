from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from .forms import ReviewForm
from .models import Review

# Create your views here.

class Reviews(FormView):
  form_class = ReviewForm
  template_name = "reviews/review.html"
  success_url = "/thank-you"
  def form_valid(self, form):
    form.save()
    return super().form_valid(form)


class ThankYou(TemplateView):
  template_name = "reviews/thank_you.html"
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context["message"]="this is working"
    return context

class SingleReviewView(DetailView):
  template_name ="reviews/single_review.html"
  model = Review
#   django automatically takes the context key as model_name in lowercase or we can use "object"

class ReviewListView(ListView):
  template_name="reviews/review_list.html"
  model = Review
  context_object_name = "reviews"
  #  django automatically takes the context key as object_list   or we can customize by using above property
  #  or attribute context_object_name="provide how we want"

  def get_queryset(self):
    query_set=super().get_queryset()
    hellow=query_set.filter(rating__gt=4)

    return hellow


# class ReviewListView(TemplateView):
#   template_name = "reviews/review_list.html"
#   def get_context_data(self, **kwargs):
#     context=super().get_context_data(**kwargs)
#     review=Review.objects.all()
#     context["reviews"]=review
#     return context

# class SingleReviewView(TemplateView):
#   template_name ="reviews/single_review.html"
#   def get_context_data(self, **kwargs):
#     context=super().get_context_data(**kwargs)
#     id=kwargs["id"]
#     selected_view=Review.objects.get(id=id)
#     context["review"]=selected_view
#     return context


# class Reviews(View):
#   def get(self,request):
#     form = ReviewForm()
#     return render(request, "reviews/review.html", {
#       "form": form
#     })
#
#
#   def post(self,request):
#     form = ReviewForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return HttpResponseRedirect("/thank-you")
#     return render(request, "reviews/review.html", {
#       "form": form
#     })
