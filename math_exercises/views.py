import random # Modulo para generar numeros aleatorios
from django.shortcuts import render


def home_view(request):    
    return render(request, 'home.html')


def Practica_Suma(request):
    return render(request, 'Practica_Suma.html')





# Generador de numeros aleatorios para la suma
def random_numbers(request):
    random_int1 = random.randint(1, 1000000000)
    random_int2 = random.randint(1, 1000000000)
    if response == random_int1 + random_int2:
        print('Correct')
        
        
        
def is_correct(request):
    if response == random_int1 + random_int2:
        return 'Correct'