pais= input('ingrese el pais')
ciudades = input('ingrese las ciudades')
array = ciudades.split(',')

for ciudad in array:
	print('Ciudad.objects.create(pais=Pais.objects.get(nombre="'+pais+'"), nombre="'+ciudad+'")')