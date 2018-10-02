from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    description = models.TextField(verbose_name = 'Descripcion')
    startOfEmployment = models.DateField(verbose_name = "Inicio de Empleo")
    exitOfEmployment = models.DateField(null=True, blank=True, verbose_name="Salida de Empleo")
    image = models.ImageField(verbose_name = 'Imagen', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de Actualización')

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title