from django.db import models

# Create your models here.
class ProjectAbout(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    description = models.TextField(verbose_name = 'Descripcion')
    image = models.ImageField(verbose_name = 'Avatar', upload_to="projectsabout")
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de Actualización')

    class Meta:
        verbose_name = "acerca de"
        verbose_name_plural = "acercas de"
        ordering = ["-created"]

    def __str__(self):
        return self.title