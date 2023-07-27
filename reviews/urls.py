from django.urls import path

from . import views

urlpatterns = [
     path("", views.Review.as_view()),
     path("thank-you", views.ThankYou.as_view())
]
