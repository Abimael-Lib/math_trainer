from django.urls import path
from .views import home_view, operacionesBasicas, estadisticas, estaticos



urlpatterns = [ 
    path("", home_view, name="home"),
    path("operacionesBasicas/", operacionesBasicas, name="operacionesBasicas"),
    path("estadisticas/<str:name>", estadisticas, name="estadisticas"),
    path("estaticos/", estaticos, name="estaticos"),
]
