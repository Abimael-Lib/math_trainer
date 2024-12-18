from django.urls import path
from . import views  



urlpatterns = [ 
    path("", views.index, name="index"),
    path("estadisticas/", views.estadisticas, name="estadisticas"),
    path("ejercicios", views.ejercicios, name="ejercicios"),
    path("estaticos/", views.estaticos, name="estaticos"),
    path("aritmetica/", views.aritmetica, name="aritmetica"),
    path("suma/", views.suma, name="suma"),
    path("create/", views.create, name="create"),
    path("delete/", views.delete, name="delete")
    
]
