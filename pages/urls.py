from django.urls import path
from .views import HomePageView, AboutPageView, PostHomePageView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about", AboutPageView.as_view(), name="about"),
    path("post", PostHomePageView.as_view(), name="posthome"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail" ),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name= "post_edit"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"), 
    path("post/<int:pk>/delete", BlogDeleteView.as_view(), name="post_delete"),
    
    ]