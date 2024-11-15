from django.urls import path
from .views import HomePageView, AboutPageView, PostHomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about", AboutPageView.as_view(), name="about"),
    path("post", PostHomePageView.as_view(), name="posthome"),
]