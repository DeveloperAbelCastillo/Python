from django.db import models

# Create your models here.
class ProjectFormacion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name = 'Título')
    especialidad = models.CharField(max_length=350, verbose_name = 'Especialidad')
    institucion = models.CharField(max_length=350, verbose_name = 'Institución')
    ubicacion = models.CharField(max_length=200, verbose_name = 'Ubicación')
    graduacion = models.IntegerField(verbose_name = 'Año de Graduacion')    
    muestragraduacion = models.BooleanField(default=True, verbose_name = '¿Mostrar Año de Graduación?')
    notaadicional = models.TextField(null=True, blank=True, verbose_name = 'Nota Adicional')
    image = models.ImageField(verbose_name = 'Imagen', upload_to="projectsformacion")
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de Actualización')

    class Meta:
        verbose_name = "formación"
        verbose_name_plural = "formaciones"
        ordering = ["-graduacion"]

    def __str__(self):
        return self.titulo