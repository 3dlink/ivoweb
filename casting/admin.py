from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Categoria, Casting

admin.site.register(Categoria)
admin.site.register(Casting)

# Register your models here.
