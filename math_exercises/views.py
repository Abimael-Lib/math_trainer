import random # Modulo para generar numeros aleatorios
from django.shortcuts import render
from .forms import NumeroForm



# Vista de la pagina principal 
def index(reuqest):
    return render(reuqest, 'index.html', {})


# Ejercicios 
def ejercicios(request):
    return render(request, 'ejercicios.html', {})



# Ejercicios/Aritmetica
def aritmetica(request):
    return render(request, 'Aritmetica.html', {})

def suma(request):
    return render(request, 'Suma.html')











def estadisticas(request):
    return render(request, 'estadisticas.html', {})




def numero_view(request):
    resultado = None
    if request.method == 'POST':
        form = NumeroForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero']
            
            resultado = numero * 2
            
    else:
        form = NumeroForm()
    
    return render(request, 'Suma.html', {'form': form, 'resultado': resultado})





def estaticos(request):
    return render(request, 'estaticos.html', {})


def herencia(request):
    return render(request, 'herencia.html', {})


