from django.db import models

from adopcion.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'vacuna'
        verbose_name_plural = 'vacunas'


    def __str__(self):
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    #image = models.ImageField(verbose_name='Imagen', upload_to='mascota', null=False, blank=False)
    persona = models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna,blank=True)

    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'

    def __str__(self):
        return '{}'.format(self.nombre)

