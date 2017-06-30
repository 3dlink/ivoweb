from django.contrib import admin

from .models import Mensaje, Experiencia, Idioma, UsuarioIdioma, Multimedia

admin.site.register(Mensaje)
admin.site.register(Experiencia)
admin.site.register(Idioma)
admin.site.register(UsuarioIdioma)
admin.site.register(Multimedia)