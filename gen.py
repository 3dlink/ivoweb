pais= input('ingrese el pais\n')
ciudades = input('ingrese las ciudades\n')
array = ciudades.split(',')

for ciudad in array:
	print('Ciudad.objects.create(pais=Pais.objects.get(nombre="'+pais+'"), nombre="'+ciudad+'")')



	#password: yCw2=@Dkd8e"$ym