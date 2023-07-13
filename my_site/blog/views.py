from django.shortcuts import render
from datetime import date
posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author":"Manju H M",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "content":"""
            Devarayanadurga or DD Hills which translates to “the fort of God”
            is a tranquil hill station located near Tumkur district in the state of Karnataka.
            Situated at an elevation of 4000 ft, Devarayanadurga is a perfect weekend getaway from Bangalore
            to live among the trees and visit the beautifully crafted temples.
        """,
        "excerpt": """
            There's nothing like the views you get when hiking in the mountains!
            And I wasn't even prepared for what happened whilst was enjoying the view!
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author":"Manju H M",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "content":"""
            Devarayanadurga or DD Hills which translates to “the fort of God”
            is a tranquil hill station located near Tumkur district in the state of Karnataka.
            Situated at an elevation of 4000 ft, Devarayanadurga is a perfect weekend getaway from Bangalore
            to live among the trees and visit the beautifully crafted temples.
        """,
        "excerpt": """
            There's nothing like the views you get when hiking in the mountains!
            And I wasn't even prepared for what happened whilst was enjoying the view!
        """
    },

    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author":"Manju H M",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "content":"""Devarayanadurga or DD Hills which translates to “the fort of God”
            is a tranquil hill station located near Tumkur district in the state of Karnataka.
            Situated at an elevation of 4000 ft, Devarayanadurga is a perfect weekend getaway from Bangalore
            to live among the trees and visit the beautifully crafted temples.""",
        "excerpt": """There's nothing like the views you get when hiking in the mountains!
             And I wasn't even prepared for what happened whilst was enjoying the view!"""
    }
]

# Create your views here.

def starting_page(request):
    return render(request,"blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request,slug):
    return render(request, "blog/post-detail.html")

