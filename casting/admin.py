from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Categoria, Casting, Audicion, Filtro

admin.site.register(Categoria)
admin.site.register(Casting)
admin.site.register(Audicion)
admin.site.register(Filtro)

# Register your models here.
