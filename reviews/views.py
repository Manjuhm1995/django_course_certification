from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review
# Create your views here.

def review(request):
  if request.method == 'POST':
    #   in order to update the values in records, get  a object of the record
    # existing_data= Review.objects.get(pk=1)
    # form = ReviewForm(request.POST,instance=existing_data)
    form = ReviewForm(request.POST)

    if form.is_valid():
      # review=Review(user_name=form.cleaned_data["user_name"],
      #               review_text=form.cleaned_data["review_text"],
      #               rating=form.cleaned_data["rating"]
      #               )
      # review.save()
      form.save()
      return HttpResponseRedirect("/thank-you")

  else:
    form = ReviewForm()

  return render(request, "reviews/review.html", {
    "form": form
  })


def thank_you(request):
  return render(request, "reviews/thank_you.html")