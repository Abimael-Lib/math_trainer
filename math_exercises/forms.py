from django import forms

class NumeroForm(forms.Form):
    numero = forms.IntegerField(label="Ingrese un número")