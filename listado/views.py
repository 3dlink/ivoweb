from django.shortcuts import render_to_response
from frontend.models import  User

# Create your views here.





def artistas(request):

    result = User.objects.filter(tipo_usuario='A')

    return render_to_response(
        "listado/artistas.html",
        {
            "artistas":result,
        },
    )

