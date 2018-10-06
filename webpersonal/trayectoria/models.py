from django.db import models

# Create your models here.
class ProjectTrayectoria(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    description = models.TextField(verbose_name = 'Descripcion')
    startOfEmployment = models.DateField(verbose_name = "Inicio de Empleo")
    exitOfEmployment = models.DateField(null=True, blank=True, verbose_name="Salida de Empleo")
    image = models.ImageField(verbose_name = 'Avatar', upload_to="projectstrayectoria")
    urlimage = models.CharField(max_length=500, verbose_name = 'Url')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de Actualización')

    class Meta:
        verbose_name = "trayectoria"
        verbose_name_plural = "trayectorias"
        ordering = ["-created"]

    def __str__(self):
        return self.title