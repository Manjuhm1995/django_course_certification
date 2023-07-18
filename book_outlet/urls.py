from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('<slug:slug>',views.book_detail,name="book_detail"),
]