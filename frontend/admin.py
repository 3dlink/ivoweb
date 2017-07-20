from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *







admin.site.register(EventoCo)
admin.site.register(GeneroArtistico)
admin.site.register(TipoArte)
admin.site.register(User)
admin.site.register(ContactCo)
admin.site.register(UsuarioArte)
admin.site.register(UsuarioArteGenero)
admin.site.register(Seguidores)
admin.site.register(Cabellos)
admin.site.register(Ojos)
admin.site.register(Etnia)
admin.site.register(Intereses)
admin.site.register(InteresesUsuario)
admin.site.register(SectorIndustria)
admin.site.register(Industria)
admin.site.register(SectorProveedor)
admin.site.register(Proveedor)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Pregunta)
