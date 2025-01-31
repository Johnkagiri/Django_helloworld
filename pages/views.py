from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

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

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = [ "title", "author", "body" ]

class BlogUpdateView(UpdateView):
    model= Post
    template_name= "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
