from django.http import HttpResponse
from django.shortcuts import render

def areaMatematica(request, area): # funcion para elegir tema de matematicas a practicar
    if area == 3:
        return HttpResponse('es el 3 pa')
    
    
def simple(request):
    return render(request, 'home.html')