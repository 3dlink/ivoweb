from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import User, TipoArte, GeneroArtistico,generateUUID, UsuarioArteGenero
from .forms import FormRegistro, FormRegistroIndustria, FormRegistroFan
from .funciones import form_invalid
import json
from casting.models import Casting
from blog.models import Post





# Create your views here.
def home(request):
    return render(request, "home.html", {})

def registrosecundario(request):
    return render(request, "registrosecundario.html",{})

def artistas(request):
    return render(request, "artistas.html",{})


def registrate(request):
    if request.method == 'POST' and request.is_ajax():
        mensaje = ''
        error = ''
        form = FormRegistro(request.POST)
        if form.is_valid():
            try:
                registro = form.save(commit =False)
                registro.uuid = generateUUID()
                registro.save()
                user = authenticate(username=registro.email, password=request.POST['password1'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        mensaje = {'mensaje': str(_('Registro realizado con exito')), 'success': True}
                    else:
                        mensaje = {'mensaje': str(_('Cuenta de usuario inactiva')), 'success': False}
                else:
                    mensaje = {'mensaje': str(_('Nombre de usuario o contraseña no valido')), 'success': False}


            except IntegrityError:
                mensaje = {
                    'mensaje': str(_('El usuario ingresado ya se encuentra registro, intente con otro por favor')),
                    'success': False}
        else:
            mensaje = form_invalid(form)

        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    context = {'from': FormRegistro}
    return render(request, "registrate.html", context)


def getArtes(request):
    if request.method == 'GET' and request.is_ajax():
        mensaje = ''
        xHTML = ''
        datos = TipoArte.objects.filter(active=True)
        if not datos:
            mensaje = ('no hay datos')
        else:
            for talento in datos:
                xHTML += '<li>'
                xHTML += '<input type="checkbox" name = "artes" id = "checkbox-' + str(talento.id) + '" value = "' + str(
                    talento.id) + '"  class="regular-checkbox" />'
                xHTML += '<label for="checkbox-' + str(talento.id) + '"></label>'
                xHTML += '<div>' + str(talento.name) + '</div>'
                xHTML += '</li>'
        return HttpResponse(json.dumps({'mensaje': mensaje, 'data': xHTML}), content_type="application/json")

    context = {'form': FormRegistro}
    return render(request, "registrate.html", context)


def getGeneroArtisticos(request):
    if request.method == 'GET' and request.is_ajax():
        mensaje = ''
        xHTML = ''
        datos = GeneroArtistico.objects.filter(id_tipo_arte=request.GET['arte'])
        if not datos:
            mensaje = ('no hay datos')
        else:
            for talento in datos:
                xHTML += '<li>'
                xHTML += '<input type="checkbox" name = "talentos[]" id = "checkbox-' + str(
                    talento.id) + '" value = "' + str(
                    talento.id) + '"  class="regular-checkbox" />'
                xHTML += '<label for="checkbox-' + str(talento.id) + '"></label>'
                xHTML += '<div>' + str(talento.name) + '</div>'
                xHTML += '</li>'
        return HttpResponse(json.dumps({'mensaje': mensaje, 'data': xHTML}), content_type="application/json")


def RegistroIndustria(request):
    if request.method == 'GET' and request.is_ajax():
        mensaje = ''
        xHTML = '<option value = "">Seleccione un sector</option>'
        datos = TipoArte.objects.filter(active=True)
        if not datos:
            mensaje = ('no hay datos')
        else:
            for sector in datos:
                xHTML += '<option value = "' + str(sector.id) + '">' + sector.name + '</option>'

        return HttpResponse(json.dumps({'mensaje': mensaje, 'data': xHTML}), content_type="application/json")

    context = {'form': FormRegistroIndustria}
    return render(request, "registraIndustria.html", context)


def industria(request):
    if request.method == 'POST' and request.is_ajax():
        mensaje = ''
        error = ''
        form = FormRegistroIndustria(request.POST)
        if form.is_valid():
            try:
                form_data = form.save(commit=False)
                username = request.POST['empresa_provedor']
                form_data.username = username.replace(' ', '')
                form_data.save()

                mensaje = {'mensaje': str(_('Registro realizado con exito')), 'success': True}
            except IntegrityError:
                mensaje = {
                    'mensaje': str(_('El usuario ingresado ya se encuentra registro, intente con otro por favor')),
                    'success': False}
        else:
            mensaje = form_invalid(form)

        return HttpResponse(json.dumps(mensaje), content_type="application/json")

    context = {'form': FormRegistroIndustria}
    return render(request, "registraIndustria.html", context)



def fan(request):
    
    if request.method == 'POST' and request.is_ajax():
        mensaje = ''
        error = ''
        form = FormRegistroFan(request.POST)
        if form.is_valid():
            try:
                
                registro = form.save(commit =False)
                registro.uuid = generateUUID()
                registro.save()
                user = authenticate(username=registro.email, password=request.POST['password1'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        mensaje = {'mensaje': str(_('Registro realizado con exito')), 'success': True}
                    else:
                        mensaje = {'mensaje': str(_('Cuenta de usuario inactiva')), 'success': False}
                else:
                    mensaje = {'mensaje': str(_('Nombre de usuario o contraseña no valido')), 'success': False}
            except IntegrityError:
                mensaje = {
                    'mensaje': str(_('El usuario ingresado ya se encuentra registrado, intente con otro por favor')),
                    'success': False}
        else:
            mensaje = form_invalid(form)

        return HttpResponse(json.dumps(mensaje), content_type="application/json")

    context = {'from': FormRegistroFan }
    return render(request, "fanatico.html", {})


def registrofan(request):

    if request.method == 'GET' and request.is_ajax():
        mensaje = ''
        xHTML = ''
        datos = TipoArte.objects.filter(active=True)
        if not datos:
            mensaje = ('no hay datos')
        else:
            for talento in datos:
                xHTML += '<li>'
                xHTML += '<input type="checkbox" name = "artes" id = "checkbox-' + str(talento.id) + '" value = "' + str(
                    talento.id) + '"  class="regular-checkbox" />'
                xHTML += '<label for="checkbox-' + str(talento.id) + '"></label>'
                xHTML += '<div>' + str(talento.name) + '</div>'
                xHTML += '</li>'
        return HttpResponse(json.dumps({'mensaje': mensaje, 'data': xHTML}), content_type="application/json")


    context = {'form': FormRegistroFan}
    return render(request, "fanatico.html", {})


def faninteres(request):
    if request.method == 'GET' and request.is_ajax():
        mensaje = ''
        xHTML = ''
        datos = GeneroArtistico.objects.filter(id_tipo_arte=request.GET['arte'])
        if not datos:
            mensaje = ('no hay datos')
        else:
            for talento in datos:
                xHTML += '<li>'
                xHTML += '<input type="checkbox" name = "talentos[]" id = "checkbox-' + str(
                    talento.id) + '" value = "' + str(
                    talento.id) + '"  class="regular-checkbox" />'
                xHTML += '<label for="checkbox-' + str(talento.id) + '"></label>'
                xHTML += '<div>' + str(talento.name) + '</div>'
                xHTML += '</li>'
        return HttpResponse(json.dumps({'mensaje': mensaje, 'data': xHTML}), content_type="application/json")
    

def proveedor(request):
    context = {'form': FormRegistroIndustria}
    return render(request, "registraProveedor.html", context)


def castings(request):
    return render(request, "castings.html", {})


def artistadashboard(request):
    posts= Post.objects.all().order_by("-fecha_creacion")[:5]
    castings = Casting.objects.all().order_by("fecha_fin")[:6]
    return render(request, "artista_dashboard.html", {"posts":posts, "castings":castings})


def industriadashboard(request):
    return render(request, "industria_dashboard.html", {})


def crearcasting(request):
    return render(request, "crear_casting.html", {})


def cerrar_sesion(request):
    logout(request)
    return redirect('/')


def index(request):
   
    if request.method == 'POST':
        if inicio_sesion(request):
            if request.GET:
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                #import pdb; pdb.set_trace()
                A=UsuarioArteGenero.objects.filter(id_usuario=request.user)
                if  (A.count() ==0 and request.user.tipo_usuario=='A'):
                    return redirect('/perfil/configuraciongeneral/')
                else:
                    return redirect ('/artistadashboard/')
        else:
            return HttpResponseRedirect(request.GET.get('next'))




def inicio_sesion(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return True
        else:
            messages.add_message(request, messages.INFO, _('Cuenta de usuario inactiva'))
            return False
    else:
        messages.add_message(request, messages.INFO, _('Nombre de usuario o contraseña no valido'))
        return False


