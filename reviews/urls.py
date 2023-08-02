from django.urls import path

from . import views

urlpatterns = [
     path("", views.Reviews.as_view()),
     path("thank-you", views.ThankYou.as_view()),
     path("review_list", views.ReviewListView.as_view()),
     path("reviews/favorite", views.AddFavoriteView.as_view()),
     path("reviews/<int:pk>", views.SingleReviewView.as_view())
]
