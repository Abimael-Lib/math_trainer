from django.shortcuts import render
from .forms import NumeroForm
from django.http import HttpResponse
from .models import Comment # clase de prueva


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





def create(request):
    comment = Comment(name="Choclo", score=5, comment="Este comentario es un comentario :v")
    
    #comment = Comment.objects.create(name="alex")
    comment.save()
    return render(request, "create.html")

def delete():
    Comment.objects.filter(id=2).delete()
    return HttpResponse("Comentario borrado")









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


