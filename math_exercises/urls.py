from django.urls import path
from .views import home_view, base_view



urlpatterns = [
    path("", home_view, name="home"),
    path("base/", base_view, name="base")
]
