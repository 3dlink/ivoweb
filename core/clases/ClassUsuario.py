from django.core.exceptions import ObjectDoesNotExist
from frontend.models import User
from perfiles.models import Experiencia, Educacion, Multimedia


class Usuario:
    __uuid = ''
    """docstring for ClassName"""

    def __init__(self, uuid):
        super(Usuario, self).__init__()
        self.__uuid = uuid

    def getDatosPersonales(self):
        usuario = User.objects.get(uuid=self.__uuid)
        return usuario

    def getExperiencia(self):
        try:
            return Experiencia.objects.filter(usuario=User.objects.get(uuid=self.__uuid))
        except ObjectDoesNotExist:
            return ''

    def getEducacion(self):
        try:
            return Educacion.objects.filter(usuario=User.objects.get(uuid=self.__uuid))
        except ObjectDoesNotExist:
            return 'no hay'

    def getGaleriaFotos(self):
        try:
            fotos = Multimedia.objects.get(usuario=User.objects.get(uuid=self.__uuid))

        except ObjectDoesNotExist:
            return ''