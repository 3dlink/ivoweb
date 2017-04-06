from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Categoria, Casting, Audicion

admin.site.register(Categoria)
admin.site.register(Casting)
admin.site.register(Audicion)

# Register your models here.
