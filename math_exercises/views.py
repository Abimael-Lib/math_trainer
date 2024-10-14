from django.shortcuts import render


def home_view(request):
    context = {
        'titulo': 'Página de inicio'
        'mensaje': 'Aplicacion de matematicas'
    }
    
    return render(request, 'templates/home.html', context)


def about_view(request):
    context = {
        'titulo': 'Graficos'
        'Mensaje': 'Graficos de desempeño'
    }
    
    return render(request, 'templates/base.html', context)