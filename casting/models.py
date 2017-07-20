from django.db import models
from frontend.models import User, Industria, Etnia, Pais, Cabellos,Ojos, TipoArte, GeneroArtistico

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
    autor = models.ForeignKey(User, blank=False)
    publico = models.BooleanField(default=True)
    #filtros
    color_cabello =  models.ForeignKey(Cabellos, blank=True, null=True)
    color_ojos =  models.ForeignKey(Ojos, blank=True, null=True)
    pais = models.ForeignKey(Pais,blank=True, null=True)
    etnia =  models.ForeignKey(Etnia,blank=True, null=True)
    tatuaje = models.NullBooleanField(blank=True, null=True, default=None)


    def __str__(self):
        return self.titulo
    @property    
    def model_name(self):
        return self._meta.verbose_name


class Filtro(models.Model):
    id_casting = models.ForeignKey(Casting, on_delete = models.CASCADE)
    id_talento = models.ForeignKey(TipoArte, on_delete = models.CASCADE)
    id_generos = models.ManyToManyField(GeneroArtistico)


class Audicion(models.Model):
    id_usuario = models.ForeignKey(User)
    id_casting = models.ForeignKey(Casting)
    motivo_participar = models.TextField()
    cuentanos = models.TextField()
    archivo =  models.FileField(upload_to='audiciones', blank=False)
    ganador = models.BooleanField(default=False)

    



# Create your models here.
