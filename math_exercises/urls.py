from django.urls import path
from .views import estadisticas, ejercicios, estaticos, index, aritmetica, suma




urlpatterns = [ 
    path("", index, name="index"),
    path("estadisticas/", estadisticas, name="estadisticas"),
    path("ejercicios", ejercicios, name="ejercicios"),
    path("estaticos/", estaticos, name="estaticos"),
    path("aritmetica/", aritmetica, name="aritmetica"),
    path("suma/", suma, name="suma"),    
]
