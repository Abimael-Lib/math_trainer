from django.urls import path
from .views import home_view, Suma



urlpatterns = [
    path("", home_view, name="home"),
    path("Suma/", Suma, name="Suma")
]
