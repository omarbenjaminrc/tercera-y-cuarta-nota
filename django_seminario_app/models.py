from django.db import models

# Create your models here.
# RESERVADO, COMPLETADA, ANULADA, NO ASISTEN

estado = [
    ('reservado','RESERVADO'),
    ('completada','COMPLETADA'),
    ('anulada','ANULADA'),
    ('no asisten','NO ASISTEN')
]
# comentario

class Inscripcion(models.Model):
    rut                 = models.CharField(max_length=12)  
    nombre              = models.CharField(max_length = 70)
    telefono            = models.IntegerField()
    fecha_inscripcion   = models.DateField()
    hora                = models.TimeField()
    institucion         = models.CharField(max_length = 70)
    estado_reserva      = models.CharField(max_length = 70,choices = estado)
    observacion         = models.TextField(blank=True)

class Institucion(models.Model):
    run                 = models.CharField(max_length=13) 
    nombre              = models.CharField(max_length = 70)