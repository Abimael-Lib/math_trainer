from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view(), name="home"),
    path("base", views.about_view, name="about")
]
