from django.urls import path
from .views import HomePageView, AboutPageView, PostHomePageView, BlogDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about", AboutPageView.as_view(), name="about"),
    path("post", PostHomePageView.as_view(), name="posthome"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail" )
    
]