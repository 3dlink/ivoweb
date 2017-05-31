from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import * 
from .forms import *
from .funciones import form_invalid
import json
from casting.models import Casting
from blog.models import Post
from perfiles.models import Mensaje
from django.core.urlresolvers import reverse
from django.db.models import Q
from itertools import chain
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings




# Create your views here.
def facebook(request):
    if request.method=='POST':


        nuevo=True;
        
        
        
        obj, created =User.objects.get_or_create(email=request.POST['email'])
       #genero=request.POST['genero'],empresa_provedor=request.POST['name'],razon_social=request.POST['name'],first_name=request.POST['first_name'], last_name=request.POST['last_name'],tipo_usuario=request.POST['tipo_usuario']
            
        
        
        if created:
            User.objects.filter(email=obj.email).update(genero=request.POST['genero'],empresa_provedor=request.POST['name'],razon_social=request.POST['name'],first_name=request.POST['first_name'], last_name=request.POST['last_name'],tipo_usuario=request.POST['tipo_usuario'])
            
            if request.POST['tipo_usuario']=='A':
                UsuarioArteGenero.objects.create(id_genero=GeneroArtistico.objects.get(id=1), id_usuario=obj)
            elif request.POST['tipo_usuario']=='I':
                SectorIndustria.objects.create(id_sector=Industria.objects.get(nombre='Productores'), id_usuario=obj)
            elif request.POST['tipo_usuario']=='P':
                SectorIndustria.objects.create(id_sector=Industria.objects.get(nombre='Iluminacion'), id_usuario=obj)
            elif request.POST['tipo_usuario']=='F':
                SectorIndustria.objects.create(id_sector=Industria.objects.get(nombre='Fanatico'), id_usuario=obj)

            obj.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, obj)            
           
        else:
            
            obj.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, obj)
            nuevo=False
            
        
        #return redirect('/perfil/configuraciongeneral/')
        return HttpResponse(json.dumps({'nuevo':nuevo,'succes':True}), content_type="application/json")    


def home(request):
    #import pdb; pdb.set_trace()
    return render(request, "home.html", {})

def registrosecundario(request):
    return render(request, "registrosecundario.html",{})

def artistas(request):
    return render(request, "artistas.html",{})


def registrate(request):
    cabellos = Cabellos.objects.all()
    ojos = Ojos.objects.all()
    etnias = Etnia.objects.all()
    artes = TipoArte.objects.all()
    generos = GeneroArtistico.objects.all()
    pais= Pais.objects.all()
    
    
    context = {'from': FormRegistro, 'cabellos':cabellos, 'ojos':ojos, 'etnias':etnias, 'artes':artes, 'generos':generos, 'paises':pais}
    return render(request, "registrate.html", context)


def buscar_ciudad(request):
    if request.method == 'POST':
        #VALIDAR QUE TENGA CIUDADES???
        ciudades = Ciudad.objects.filter(pais=Pais.objects.get(id=request.POST['id_pais']))
        #import pdb; pdb.set_trace()
        xHTML='<option selected="selected" disabled>Ciudad de Residencia</option> '
        for ciudad in ciudades:
            xHTML+='<option value="'+ciudad.nombre+'">'+ciudad.nombre+'</option>'


        context={'xHTML':xHTML,                
                'success': True}

        
        return HttpResponse(json.dumps(context), content_type="application/json")    

def registrate_artistas(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        mensaje = ''
        error = ''
        form = FormRegistro(request.POST) 
        if form.is_valid():
            try:
                registro = form.save(commit=False)
                registro.uuid = generateUUID()
                registro.save()
                user = authenticate(username=registro.email, password=request.POST['password1'])
                if user is not None:
                    if user.is_active:
                        if request.POST['talento'] != '':
                            UsuarioArteGenero.objects.create(id_genero=GeneroArtistico.objects.get(id=request.POST['generoarte']), id_usuario=user)
                            
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
        #return redirect('/perfil/configuraciongeneral/')



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
        #datos = TipoArte.objects.filter(active=True)
        datos = Industria.objects.filter(tipo='I')
        if not datos:
            mensaje = ('no hay datos')
        else:
            for sector in datos:
                xHTML += '<option value = "' + str(sector.id) + '">' + sector.nombre + '</option>'

        return HttpResponse(json.dumps({'mensaje': mensaje, 'data': xHTML}), content_type="application/json")
    sectores = Industria.objects.filter(tipo='I')
    pais= Pais.objects.all()
    context = {'form': FormRegistroIndustria,'sectores':sectores,'paises':pais }
    
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
                form_data.uuid = generateUUID()
                form_data.save()

                user = authenticate(username=form_data.email, password=request.POST['password1'])
                if user is not None:
                    if user.is_active:
                        if request.POST['sector'] != '':
                            SectorIndustria.objects.create(id_sector=Industria.objects.get(id=request.POST['sector']), id_usuario=user)

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
    sectores = Industria.objects.filter(tipo='I')
    pais= Pais.objects.all()
    context = {'form': FormRegistroIndustria, 'sectores':sectores, 'paises': pais}
    return render(request, "registraIndustria.html", context)


#REVISAR ESTOS INTERERES
def fan(request):
    intereses = TipoArte.objects.all()    
    context = {'from': FormRegistroFan, 'intereses':intereses}
    return render(request, "fanatico.html", context)


def registrofan(request):
    if request.method == 'POST':
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
                        SectorIndustria.objects.create(id_sector=Industria.objects.filter(tipo='F')[0].id, id_usuario=user)
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
    

def RegistroProveedor(request):
    # datos = Industria.objects.filter(tipo='I')
    # context = {'form': FormRegistroIndustria,'sectores':datos}
    # return render(request, "registroproveedor.html", context)
    if request.method == 'GET' and request.is_ajax():
        mensaje = ''
        xHTML = '<option value = "">Seleccione un sector</option>'
        #datos = TipoArte.objects.filter(active=True)
        datos = Industria.objects.filter(tipo='P')
        if not datos:
            mensaje = ('no hay datos')
        else:
            for sector in datos:
                xHTML += '<option value = "' + str(sector.id) + '">' + sector.nombre + '</option>'

        return HttpResponse(json.dumps({'mensaje': mensaje, 'data': xHTML}), content_type="application/json")
    sectores = Industria.objects.filter(tipo='P')
    pais= Pais.objects.all()
    context = {'form': FormRegistroIndustria,'sectores':sectores,'paises':pais}
    
    return render(request, "registroproveedor.html", context)


def castings(request):
    return render(request, "castings.html", {})


def artistadashboard(request):

    
    if request.user.tipo_usuario=="A":
        #DEBERIA HACERLO DE LA USUARIO-ARTE
        generos = UsuarioArteGenero.objects.filter(id_usuario=request.user)
        posts= Post.objects.all().order_by("-fecha_creacion")[:5]
        castings = Casting.objects.all().order_by("fecha_fin")[:6]
        siguiendo = Seguidores.objects.filter(origen=request.user)[:5]
        seguidores = Seguidores.objects.filter(destino=request.user)[:5]
        numero_seguidores =len(Seguidores.objects.filter(destino=request.user))
        enviados = Mensaje.objects.filter(origen=request.user.id)
        recibidos = Mensaje.objects.filter(destino=request.user.id)
        industrias = Industria.objects.all()
        proveedores = SectorIndustria.objects.filter(id_sector__in=Industria.objects.filter(tipo='P').values_list('id',flat=True))[:4]
        paises=Pais.objects.all()
        

        if len(generos)>0:
            genero= generos[0]
        else:
            genero=''
        return render(request, "dashboard/artista.html", {'paises':paises,"posts":posts, "castings":castings, "siguiendo":siguiendo, "seguidores":seguidores, "genero":genero, 'enviados':enviados,'recibidos':recibidos, 'fans':numero_seguidores,'industrias': industrias, 'proveedores':proveedores })

    else:
       
        profesion = SectorIndustria.objects.get(id_usuario=request.user)
        posts= Post.objects.all().order_by("-fecha_creacion")[:5]       
        siguiendo = Seguidores.objects.filter(origen=request.user)[:5]
        seguidores = Seguidores.objects.filter(destino=request.user)[:5]
        numero_seguidores = len(Seguidores.objects.filter(destino=request.user))
        talentos = UsuarioArteGenero.objects.all()[:8]
        enviados = Mensaje.objects.filter(origen=request.user.id)
        recibidos = Mensaje.objects.filter(destino=request.user.id)
        proveedores = SectorIndustria.objects.filter(id_sector__in=Industria.objects.filter(tipo='P').values_list('id',flat=True))[:4]
        industrias = Industria.objects.filter(tipo='P')
        artes = TipoArte.objects.all()
        cabellos = Cabellos.objects.all()
        ojos = Ojos.objects.all()
        etnias = Etnia.objects.all()
        paises=Pais.objects.all()
        


        context= {
        'paises':paises,
        "posts":posts, 
        "talentos":talentos, 
        "siguiendo":siguiendo, 
        "seguidores":seguidores,
        'enviados':enviados,
        'recibidos':recibidos,
        'fans':numero_seguidores,
        'profesion':profesion, 
        'proveedores':proveedores, 
        'industrias': industrias,
        'artes':artes,
        'cabellos':cabellos,
        'ojos':ojos,
        'etnias':etnias}
        
        #import pdb; pdb.set_trace()
        return render(request, "dashboard/industria.html", context )

def industriadashboard(request):
    return render(request, "industria_dashboard.html", {})


def crearcasting(request):
    return render(request, "crear_casting.html", {})


def cerrar_sesion(request):
    logout(request)
    return redirect('/')


def index1(request):
   
    if request.method == 'POST':
        if inicio_sesion(request):
            #import pdb; pdb.set_trace()
            if request.GET:
                
                print ("entrando en LUGAR DESCONOCIDO")
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                
                if request.user.tipo_usuario== 'A':
                    print ("entrando como artista")
                    A=UsuarioArteGenero.objects.filter(id_usuario=request.user)
                    if  (A.count() ==0 and request.user.tipo_usuario=='A'):
                        print ("primera vez artista")
                        return redirect('/perfil/configuraciongeneral/')
                    else:
                        print ("xxxx vez artista")
                        return redirect ('/artistadashboard/')
                else:
                    print ("entrando como industria por primera vez")
                    return redirect('/perfil/configuraciongeneral/')
        else:
            print ("entrando como NO SE QUE")
            return HttpResponse("Nombre de usuario o contraseña no valido")
            #return HttpResponseRedirect(request.GET.get('next'))


def index(request):
    #import pdb; pdb.set_trace()
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            if user.tipo_usuario== 'A':
                    #print ("entrando como artista")
                A=UsuarioArteGenero.objects.filter(id_usuario=user)
                if  (A.count() ==0 ):
                    print ("primera vez artista")
                    return redirect('/perfil/configuraciongeneral/')
                else:
                    print ("xxxx vez artista")
                    return redirect ('/artistadashboard/')
            else:
                    #VER COMO VALIDO QUE SEAN LAS PROXIMAS ENTRADAS DE LA INDUSTRIA
                return redirect('/perfil/configuraciongeneral/')
    #return render(request.META['HTTP_REFERER'], {'login_form': form })

    return render (request, "home.html", {'login_form': form })


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


def seguir(request):       
    if request.method == 'POST':
        if (request.POST['origen'] != request.POST['destino']):
            #import pdb; pdb.set_trace()
            if(len(Seguidores.objects.filter(origen=request.POST['origen'], destino=request.POST['destino'])) == 0):
                mensaje=''
                form = FormSeguir(request.POST)
                if form.is_valid():
                    form.save()
                    mensaje = {'mensaje': str(_('Siguiendo usuario')), 'success': True}       
                else:
                     mensaje = {'mensaje': str(_('No se ha podido seguir el usuario')), 'success': False}
            else:
                #  AQUI ESTARIA LA LOGICA PARA BORRAR Y ELIMINAR EL SEGUIMIENTO
                Seguidores.objects.filter(origen=request.POST['origen'], destino=request.POST['destino']).delete()

                mensaje = {'mensaje': str(_('Ya no sigues al usuario')), 'success': True} 
        else:
            mensaje = {'mensaje': str(_('No te puedes seguir tu mismo')), 'success': False} 
    return HttpResponse(json.dumps(mensaje), content_type="application/json")


def busqueda_avanzada(request):
    if request.method == 'POST':

        if request.user.tipo_usuario == 'A':
            results_ind = SectorIndustria.objects.all()
            results_usr = User.objects.filter(tipo_usuario='I')|User.objects.filter(tipo_usuario='P')
            #results_pro = SectorProveedor.objects.all()
            ind = Q(id_sector=0) | Q(id_sector=99)
            usr = Q(pais=400) | Q(pais=401)
            #pro = Q(id_sector=0) | Q(id_sector=99)
            for key in request.POST.keys():                
                if key != 'csrfmiddlewaretoken':
                    if key.split('-')[0] == 'usr':
                        if key.split('-')[1] == 'pais':
                                if request.POST[key] != '':
                                    usr.add((Q(pais=request.POST[key])),usr.OR)
                    else:            
                        ind.add((Q(id_sector=key.split('-')[1])),ind.OR)

            results_usr = results_usr.filter(usr).values_list('id', flat=True)

            results = results_ind.filter(ind) | SectorIndustria.objects.filter(id_usuario__in=results_usr)

            import pdb; pdb.set_trace()
        else:
            control = 0
            #results_final = UsuarioArteGenero.objects.all()
            result_art = TipoArte.objects.all()
            results_usr = User.objects.filter(tipo_usuario='A')
            results_ind = SectorIndustria.objects.all()
            #results_pro = SectorProveedor.objects.all()
            ind = Q(id_sector=0) | Q(id_sector=99)
            usr = Q(color_cabello=99) | Q( color_ojos=0)
            art = Q(id=99) | Q(id=0)
            #pro = Q(id_sector=0) | Q(id_sector=99)
            for key in request.POST.keys():                
                if key != 'csrfmiddlewaretoken':
                        if key.split('-')[0] == 'art':
                            art.add((Q(id=key.split('-')[1])),art.OR)
                        elif key.split('-')[0] == 'usr':
                            if key.split('-')[1] == 'color_ojos':
                                if request.POST[key] != '':
                                    usr.add((Q(color_ojos=request.POST[key])),usr.OR)
                            elif key.split('-')[1] == 'color_cabello':
                                if request.POST[key] != '':
                                    usr.add((Q(color_cabello=request.POST[key])),usr.OR)
                            elif key.split('-')[1] == 'etnia':
                                if request.POST[key] != '':
                                    usr.add((Q(etnia=request.POST[key])),usr.OR)
                            elif key.split('-')[1] == 'pais':
                                if request.POST[key] != '':
                                    usr.add((Q(pais=request.POST[key])),usr.OR)
                            elif key.split('-')[1] == 'agencia':
                                usr.add((Q(agencia__isnull=False)),usr.OR)
                            elif key.split('-')[1] == 'viajar':
                                usr.add((Q(disponible_viajes=True)),usr.OR)
                            elif key.split('-')[1] == 'tatuaje':
                                usr.add((Q(tatuaje=True)),usr.OR)
                            elif key.split('-')[1] == 'pasaporte':
                                usr.add((Q(pasaporte__isnull=False)),usr.OR)
                            elif key.split('-')[1] == 'visa':
                                usr.add((Q(visa__isnull=False)),usr.OR)
                        else:
                            control=1
                            ind.add((Q(id_sector=key.split('-')[1])),ind.OR)


            if control == 0:            
                result_art = result_art.filter(art).values_list('id', flat=True)
                generos = GeneroArtistico.objects.filter(id_tipo_arte__in=result_art)
                #
                results_usr = results_usr.filter(usr).values_list('id', flat=True)
                results = UsuarioArteGenero.objects.filter(id_usuario__in=results_usr) | UsuarioArteGenero.objects.filter(id_genero__in=generos)
            else:
                results = results_ind.filter(ind)

    #import pdb; pdb.set_trace()            
    return render(request, 'dashboard/busqueda_avanzada.html',{'results':results})


def get_user(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        users = User.objects.filter(email__icontains = q )[:20]
        results = []
        for user in users:
            user_json = {}
            user_json['id'] = user.id
            user_json['label'] = user.email
            user_json['value'] = user.email
            results.append(user_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def olvidoclave(request):
    return render(request, "olvido-clave.html", {})

def terminos(request):
    return render(request, "estaticas/terminos.html", {})


def planes(request):
    return render(request, "estaticas/planes.html", {})

def faq(request):
    return render(request, "estaticas/faq.html", {})

def faqpregunta(request):
    return render(request, "estaticas/faq-pregunta.html", {})

def corporativa(request):
    form = contactoForm
    return render(request, "estaticas/corporativa.html", {'form':form})


def contacto(request):
    form = contactoForm
    if request.method == 'POST':
        
        form = contactoForm(request.POST)       
       
        if form.is_valid():
            subject = form.cleaned_data['asunto']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['mensaje']
            name= form.cleaned_data['nombre']
            try:
                send_mail(subject, name+'\n\n'+message, from_email, ['ivotalents@gmail.com','ati2mortiz@gmail.com'])
                return redirect('/corporativa/')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')           

    return render(request, "estaticas/corporativa.html", {'form':form})
