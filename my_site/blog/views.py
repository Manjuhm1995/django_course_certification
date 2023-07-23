from django.shortcuts import render,get_object_or_404
from .models import Post,Tag,Author

# Create your views here.

def starting_page(request):
    latests_posts=Post.objects.all().order_by("-date")[:3]
    # it just reduce the performance because just for 3 we are fething
    # all posts and filtering and slicing in python

    return render(request,"blog/index.html",{"posts":latests_posts})

def posts(request):
    latests_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html",{"posts":latests_posts})


def post_detail(request,slug):
    # identified_post=Post.objects.get(slug=slug)
    # above line may lead to the error so we need to use the try except block
    # below line provide the same functionality without much code

    identified_post=get_object_or_404(Post,slug=slug)
    return render(request, "blog/post-detail.html",{"posts":identified_post})

