from django.db import models

# Create your models here.

class Parroquia(models.Model):
    

    nombre = models.CharField(max_length=60)   
    tipo_parroquia = models.CharField(max_length=30) 

    def __str__(self):
        return "%s - %s" % (self.nombre, 
                self.tipo_parroquia)


class Barrio(models.Model):          
        
    opciones_parques = (
        (1,'Un Parque'),
        (2,'Dos Parques'),
        (3,'Tres Parques'),
        (4,'Cuatro Parques'),
        (5,'Cinco Parques'),
        (6,'Seis Parques'),       
        )

    nombre = models.CharField(max_length=60) 
    viviendas = models.IntegerField("numero de viviendas")
    parques = models.IntegerField("numero de parques", choices=opciones_parques)
    edificios = models.IntegerField("numero de edificios")
    parroquia = models.ForeignKey(Parroquia, related_name='barrios', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %s - %s" % (self.nombre, 
                self.viviendas,
                self.parques,
                self.edificios)