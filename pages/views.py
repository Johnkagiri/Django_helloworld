from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here.

# def homePageView(request):
#     return HttpResponse("hello world")

class HomePageView(TemplateView):
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name= "about.html" 

class PostHomePageView(ListView):
    model = Post
    template_name = "posthome.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"