from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
    	return self.nombre


class Post(models.Model):	
	imagen = models.ImageField( blank=True)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	categoria = models.ForeignKey(Categoria)
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.titulo
