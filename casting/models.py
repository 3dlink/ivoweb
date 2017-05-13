from django.db import models
from frontend.models import User, Industria

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
    	return self.nombre

class Casting(models.Model):
    titulo = models.CharField(max_length=255, blank=False)  # Field name made lowercase.
    fecha_inicio = models.DateTimeField(null=False)  # Field name made lowercase.
    fecha_fin = models.DateTimeField(null=False)  # Field name made lowercase.
    modifiedon = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(auto_now_add=True ,auto_now=False, null=True)  # Field name made lowercase.
    imagen_principal = models.ImageField( upload_to='casting',blank=True)
    imagen_1 = models.ImageField(upload_to='casting', blank=True)
    imagen_2 = models.ImageField(upload_to='casting', blank=True)
    descripcion = models.TextField()
    info_destacada = models.TextField()
    info_adicional = models.TextField()
    descripcion_breve= models.CharField(max_length=255, blank=False)
    autor = models.ForeignKey(User)
    categoria = models.ForeignKey(Industria)


    def __str__(self):
        return self.titulo

class Audicion(models.Model):
    id_usuario = models.ForeignKey(User)
    id_casting = models.ForeignKey(Casting)
    motivo_participar = models.TextField()
    cuentanos = models.TextField()
    archivo =  models.FileField(upload_to='audiciones', blank=False)
    ganador = models.BooleanField(default=False)

    



# Create your models here.
