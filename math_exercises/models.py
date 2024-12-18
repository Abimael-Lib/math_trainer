from django.db import models

# clase para ver la respuesta dada es correcta o incorrecta
class Ejercicio(models.Model):
    name = models.CharField(max_length=25, null=False) # tipo de ejercicio
    score  = models.IntegerField(null=False)
    
    def __str__(self):
        return str(self.name)
    

class Comment(models.Model): # Clase de prueva
    name = models.CharField(max_length=50, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=100, default="Firma")