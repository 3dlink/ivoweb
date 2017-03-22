from django.db import models
from django.utils.translation import ugettext_lazy as _
from frontend.models import User
# Create your models here.

class Experiencia(models.Model):
    empresa = models.CharField(max_length=100, null=False, blank=False, verbose_name= _('Empresa'))
    cargo = models.CharField(max_length=100, null=False, blank=False, verbose_name= _('Cargo'))
    fecha_desde = models.DateField(null=False, blank=False, verbose_name=_('Desde'))
    fecha_hasta = models.DateField(null=True, blank=True, verbose_name=_('Desde'))
    trabajo_actual = models.BooleanField(default=False, verbose_name=_('Laborando actualmente?'))
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiencia')


    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
        db_table = 'Experiencia_usuario'


class Educacion(models.Model):
    institucion = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Centro de Estudios'))
    fecha_inicio_estudio = models.DateField(null=False, blank=False, verbose_name=_('Fecha inicio estudios'))
    fecha_fin_estudio = models.DateField(null=True, blank=True, verbose_name=_('Fecha culmino estudios'))
    estudiando_actualmente = models.BooleanField(default=False, verbose_name=_('Estudiando actualmente'))
    titulo =models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Titulo'))
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educacion')

    class Meta:
        verbose_name = 'Educacion'
        verbose_name_plural = 'Educacion'
        db_table = 'Educacion_usuario'


class Multimedia(models.Model):
    cluster = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Culster'))
    archivo = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Archivo'))
    nombre_archivo = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Nombre del Archivo'))
    tipo_archivo = models.CharField(max_length=1, null=False, blank=False, verbose_name=_('Tipo de archivo'))
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='multimedia')
    estado = models.CharField(max_length=1, default='R', verbose_name=_('Estado del archivo'))

    def absolute_url(self):
        return "/media/%s%s/" % (self.cluster, self.archivo)

    class Meta:
        db_table = 'Archivos_multimedia'
        verbose_name = 'Archivo Multimedia'
        verbose_name_plural = 'Archivos Multimedia'