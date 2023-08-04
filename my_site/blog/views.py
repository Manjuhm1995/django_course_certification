from django.shortcuts import render,get_object_or_404
from .models import Post,Tag,Author
from django.views.generic import ListView,DetailView
from .forms import CommentForm
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
class StartingPageView(ListView):
    template_name ="blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    def get_queryset(self):
        query_set=super().get_queryset()
        data=query_set[0:3]
        return data

class AllPostView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    ordering = ["-date"]
    context_object_name = "posts"


# class SinglePostView(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["posts_tags"]=self.object.tags.all()
#         context["posts"]=self.object
#         context["comment_form"]=CommentForm()
#
#         return context
class SinglePostView(View):
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        context={
            "posts":post,
            "posts_tags":post.tags.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id")
        }

        return render(request,"blog/post-detail.html",context)
    def post(self,request,slug):
        post = Post.objects.get(slug=slug)
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        context = {
            "posts": post,
            "posts_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")

        }
        return render(request,"blog/post-detail.html",context)

class ReadLaterView(View):
    def get(self,request):
        stored_posts=request.session.get("stored_posts")
        context={}
        if stored_posts is None or len(stored_posts)==0:
            context["has_posts"]=False
            context["posts"]=[]
        else:
            context["posts"]=Post.objects.filter(id__in=stored_posts)
            context["has_posts"]=True
        return render(request, "blog/stored_posts.html", context)

    def post(self,request):
        post_id=request.POST["post_id"]
        stored_posts=request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts=[]
        if post_id not in stored_posts:
            stored_posts.append(int(post_id))
            request.session["stored_posts"]=stored_posts
        return HttpResponseRedirect("/")
