

def getDatosActualizar( modelo, request):
    '''
    Sirve para extraer campos y el valor que se desea que tenga para luego usar el ORM de django para actualizar
    esos campos especificos.

    :param modelo: Modelo al que se le quiere extraer los campos
    :param request: peticion HTTP
    :return: retorna una lista con clave valor, siendo clave el campo y el valor seia el valor en cuestion que tendra
    el campo
    '''
    array_campo = str(modelo._meta.get_fields()).split(',')
    campos_actualizar = {}
    for campo_modelo in array_campo:
        campo = str(campo_modelo).split(':')
        field = campo[1].replace('>','').replace(')','').strip()

        if field in request.POST:
            if len(request.POST[field]) > 0:
                campos_actualizar[field] = request.POST[field]

    return campos_actualizar