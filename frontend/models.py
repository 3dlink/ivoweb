#encoding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core import validators
from django.utils import timezone
from django.utils.http import urlquote
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from uuid import uuid4
# Create your models here.




def generateUUID():
    return str(uuid4())

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    INDUSTRIA = 'I'
    ARTISTAS = 'A'
    FANS = 'F'
    TIPO_USUARIO = (
        (INDUSTRIA, 'INDUSTRIA'),
        (ARTISTAS, 'ARTISTAS'),
        (FANS, 'FANS'),
    )

    avatar = models.ImageField(upload_to='avatar', blank=True, null=True, max_length=200)
    telefono = models.BigIntegerField(verbose_name='Numero de telefono', blank=True, null=True, db_column='Telefono')
    genero = models.CharField(max_length=1, blank=True, null=True, db_column='Genero')
    tatuaje = models.BooleanField(default=False, db_column='Tatuaje')
    color_cabello = models.CharField(max_length=60, blank=True, null=True, verbose_name=_('Color de cabello'),
                                     db_column='Colorcabello')
    color_ojos = models.CharField(max_length=60, blank=True, null=True, verbose_name=_('Color de ojos'),
                                  db_column='Colorojo')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name=_('Fecha de nacimiento'),
                                        db_column='Fechanacimiento')
    nacionalidad = models.CharField(max_length=60, blank=True, null=True, verbose_name=_('Nacionalidad'),
                                    db_column='Nacionalidad')
    pais = models.CharField(max_length=60, blank=False, null=False, verbose_name=_('Pais'), db_column='Pais')
    ciudad = models.CharField(max_length=60, blank=True, null=True, verbose_name=_('Ciudad'), db_column='Ciudad')
    etnia = models.CharField(max_length=40, blank=True, null=True, verbose_name=_('Etnia'), db_column='Etnia')
    pasaporte = models.CharField(max_length=60, blank=True, null=True, verbose_name=_('Pasaporte'),
                                 db_column='Pasaporte')
    visa = models.CharField(max_length=60, blank=True, null=True, verbose_name=_('Visa'), db_column='Visa')
    facebook = models.CharField(max_length=80, blank=True, null=True, verbose_name='Facebook', db_column='Facebook')
    twitter = models.CharField(max_length=80, blank=True, null=True, verbose_name='Twitter', db_column='Twitter')
    instagram = models.CharField(max_length=80, blank=True, null=True, verbose_name='Instagram', db_column='Instagram')
    agencia = models.CharField(max_length=40, blank=True, null=True, verbose_name=_('Agencia / Manager'),
                               db_column='Agencia')
    empresa_provedor = models.CharField(max_length=80, db_index=True, blank=False,null=True,
                                        db_column='Empresaproveedor')  # puede ser una empreas o proveedor
    razon_social = models.CharField(max_length=80, null=True, blank=True,
                                    db_column='Razonsocial')  # puede ser una empreas o proveedor
    direccion = models.CharField(max_length=200, null=True, blank=True, db_column='Direccion',
                                 verbose_name=_('Direccion'))
    website = models.CharField(max_length=100, null=True, blank=True, db_column='Website', verbose_name=_('Sitio web'))
    tipo_usuario = models.CharField(max_length=1, null=False, blank=False, default='A', choices=TIPO_USUARIO,
                                    db_column='Tipousuario', verbose_name=_('Tipo de usuario'))
    uuid = models.CharField( unique=True, max_length=100, default= generateUUID())
    biografia = models.TextField(db_column='Biografia', null=True, blank=True, verbose_name=_('Biografia'))
    disponible_viajes = models.BooleanField(default=False, verbose_name='Disponibilidad de viaje')
    idioma = models.CharField(max_length=60,null=True, blank=True, verbose_name=_('Idiomas'))
    usuario = models.CharField(max_length=60,null=True, blank=True, verbose_name=_('ID-Usuario'))
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.
    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(('active'), default=True,
        help_text=('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = ('Usuarios')

    @property
    def get_avatar(self):
        return str(self.avatar)
        #.replace('avatar/', 'avatar/sm_')

    def get_uuid(self):
        return self.uuid

    def get_absolute_url(self):
        return "/perfil/%s/" % (self.uuid)

    def get_api_url(self):
       return "/api/v1/%s/" % (self.uuid)


    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        #Sends an email to this User.
        send_mail(subject, message, from_email, [self.email])

    def get_tipo_usuario(self):
        return self.tipo_usuario

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)



class EventoCo(models.Model):
    ids = models.AutoField(db_column='IDs', primary_key=True, editable=False)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True, verbose_name="Nombre")  # Field name made lowercase.
    fechaInicio = models.DateTimeField(db_column='FechaInicio', null=True)  # Field name made lowercase.
    fechaFin = models.DateTimeField(db_column='FechaFin', null=True)  # Field name made lowercase.
    modifiedon = models.DateTimeField(db_column='Modifiedon', auto_now_add=False, auto_now=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='Createdon',  auto_now_add=True ,auto_now=False, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        #managed = False
        db_table = 'Evento_co'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'


class ContactCo(models.Model):
    ids = models.AutoField(db_column='IDs', primary_key=True, editable=False)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True, verbose_name="Nombre")  # Field name made lowercase.
    middlename = models.CharField(db_column='Middlename', max_length=255, blank=True, null=True, verbose_name="Segundo Nombre" )  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255, blank=True, null=True, verbose_name="Apellido")  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday', blank=True, null=True , verbose_name="Fecha Cumpleaños")  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', default=True)  # Field name made lowercase. This field type is a guess.
    modifiedon = models.DateTimeField(db_column='Modifiedon', auto_now_add=False, auto_now=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='Createdon',  auto_now_add=True ,auto_now=False, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        #managed = False
        db_table = 'Contact_co'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'


class TipoArte(models.Model):
    name = models.CharField(_('Tipo de Arte'), max_length=255, blank=True)
    active = models.BooleanField(default=True)
    createdOn = models.DateTimeField(_('created On'),auto_now_add=True, auto_now=False)
    modifiedOn = models.DateTimeField(_('modified On'),auto_now_add=False, auto_now=True)

    class Meta:
        db_table = 'TipoArte_co'
        verbose_name = ('Tipo de Arte')
        verbose_name_plural = ('Tipos de Arte')

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class GeneroArtistico(models.Model):
    name = models.CharField(_('Genero Artistico'), max_length=255, blank=True)
    id_tipo_arte = models.ForeignKey(TipoArte, on_delete=models.CASCADE, related_name='artegenero')
    createdOn = models.DateTimeField(_('created On'),auto_now_add=True, auto_now=False)
    modifiedOn = models.DateTimeField(_('modified On'),auto_now_add=False, auto_now=True)

    class Meta:
        db_table = 'GeneroArtistico_co'
        verbose_name = _('Genero')
        verbose_name_plural = ('Generos')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return '%s' % (self.name)




class UsuarioArte(models.Model):
    id_arte = models.ForeignKey(TipoArte, db_column='Idtalento', on_delete=models.CASCADE, null=True, related_name='tipo_arte')
    id_usuario = models.ForeignKey(User, db_column='Idusuario', on_delete=models.CASCADE, null=True, related_name='user_arte')
    class Meta:
        db_table = 'InteresUsuario'
        verbose_name = 'Interes del usuario'
        verbose_name_plural = 'Intereses del usuario'

    @property
    def get_arte(self):
        return self.id_arte

    def get_usuario(self):
        return self.id_usuario



class UsuarioArteGenero(models.Model):
    id_usuario = models.ForeignKey(User, db_column='Idusuario', on_delete=models.CASCADE, null=True,related_name='user_genero')
    id_genero = models.ForeignKey(GeneroArtistico, on_delete=models.CASCADE, related_name='genero')
    createdOn = models.DateTimeField(_('created On'),auto_now_add=True, auto_now=False)
    modifiedOn = models.DateTimeField(_('modified On'),auto_now_add=False, auto_now=True)
    class Meta:        
        verbose_name = _('RelacionGeneroARTE')
        verbose_name_plural = ('RelacionGenerosARTES')

    @property
    def get_genero(self):
        return self.id_genero

    def get_usuario(self):
        return self.id_usuario

    def __unicode__(self):
        return '%s' % (self.id_genero.name)


#class Seguidores(models.Model):
 #   destino= models.ForeignKey(User, on_delete=models.CASCADE, related_name="siguiendo")
  #  origen= models.ForeignKey(User, on_delete=models.CASCADE,related_name="seguidores")