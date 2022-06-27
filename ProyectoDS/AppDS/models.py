from django.db import models

# Create your models here.
class Chofer(models.Model):

    nombre=models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    transporte = models.CharField(max_length=60)
    contacto= models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido : {self.apellido} - Transporte : {self.transporte} - E-mail : {self.contacto}"


class Unidad(models.Model):
    tractor= models.CharField(max_length=7)
    semi= models.CharField(max_length=15)
    tipo= models.CharField(max_length=15)

class Bobina(models.Model):
    numero= models.CharField(max_length=30)
    cliente= models.CharField(max_length=20)
    buque= models.CharField(max_length=20)
    criticidad= models.CharField(max_length=10)
    peso= models.IntegerField()
    ancho= models.IntegerField()

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Bobina n°: {self.numero} - Cliente {self.cliente} - Criticidad {self.criticidad} - Peso {self.peso}"

