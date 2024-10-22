from django.urls import path
from .views import home_view, Practica_Suma



urlpatterns = [
    path("", home_view, name="home"),
    path("Practica_Suma/", Practica_Suma, name="Practica_Suma")
]
