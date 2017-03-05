from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import ContactCo
from .models import TipoArte
from .models import GeneroArtistico
from .models import User
from .models import EventoCo
from .models import UsuarioArte
from .models import UsuarioArteGenero







admin.site.register(EventoCo)
admin.site.register(GeneroArtistico)
admin.site.register(TipoArte)
admin.site.register(User)
admin.site.register(ContactCo)
admin.site.register(UsuarioArte)
admin.site.register(UsuarioArteGenero)


