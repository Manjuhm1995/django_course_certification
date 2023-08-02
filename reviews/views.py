from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,FormView
from .forms import ReviewForm
from .models import Review

# Create your views here.

class Reviews(CreateView):
  model = Review
  form_class = ReviewForm
  # fields = "__all__" #if we use this property we no need to create
  # formclass by inheriting the ModelForm class
  template_name = "reviews/review.html"
  success_url = "/thank-you"
# class Reviews(FormView):
#   form_class = ReviewForm
#   template_name = "reviews/review.html"
#   success_url = "/thank-you"
#   def form_valid(self, form):
#     form.save()
#     return super().form_valid(form)


class ThankYou(TemplateView):
  template_name = "reviews/thank_you.html"
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context["message"]="this is working"
    return context

class SingleReviewView(DetailView):
  template_name ="reviews/single_review.html"
  model = Review

  def get_context_data(self, **kwargs):
    context= super().get_context_data(**kwargs)
    loaded_object=self.object
    request=self.request
    favourite_id=request.session["favorite_review"]
    context["is_favourite"]=favourite_id==str(loaded_object.id)
    return context
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

class AddFavoriteView(View):
  def post(self,request):
    review_id=request.POST["review_id"]
    # fav_review=Review.objects.get(pk=review_id)
    request.session["favorite_review"]=review_id
    return HttpResponseRedirect("/reviews/" + review_id)
