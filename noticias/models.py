from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField (max_length=200, verbose_name= "Titulo")
    description= models.TextField(verbose_name= "Descripcion")
    image = models.ImageField(verbose_name= "Imagen", upload_to="projects")
    created = models.DateTimeField (auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField (auto_now=True, verbose_name= "Fecha de modificacion")
    link = models.URLField(verbose_name="Sitio web", null=True, blank= True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ["-created"]
        