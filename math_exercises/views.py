import random # Modulo para generar numeros aleatorios
from django.shortcuts import render
from .forms import NumeroForm



# Vista de la pagina principal 
def home_view(request):    
    return render(request, 'home.html')

# Vista de la pagina de Suma
def Suma(request):
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



