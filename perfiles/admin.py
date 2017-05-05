from django.contrib import admin

from .models import Mensaje, Experiencia, Idioma, UsuarioIdioma

admin.site.register(Mensaje)
admin.site.register(Experiencia)
admin.site.register(Idioma)
admin.site.register(UsuarioIdioma)