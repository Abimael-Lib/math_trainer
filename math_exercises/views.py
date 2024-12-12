import random # Modulo para generar numeros aleatorios
from django.shortcuts import render
from .forms import NumeroForm



# Vista de la pagina principal 
def home_view(request):    
    return render(request, 'home.html')

# Vista de la pagina de seleccion de operaciones
def operacionesBasicas(request, operacion): # usar argumentos para seleccionar la operacion
    if operacion == 'Suma': 
        return render(request, 'Suma.html') 


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

def estadisticas(request, name):
    categories = ['operaciones', 'numeros']
    context = {'name': name, 'categories': categories}
    return render(request, 'Estadisticas.html', context)

def estaticos(request):
    return render(request, 'estaticos.html', {})