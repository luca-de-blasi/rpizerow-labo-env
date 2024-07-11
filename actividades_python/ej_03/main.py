from gpiozero import LED, Buzzer

#Defino un pin para cada led
rojo = LED(19)
verde = LED(13)
azul = LED(26)
buzzer = Buzzer (22)

while True:
	#Pido al usuario que escriba un comando y luego una funcion
	comando = input ("Ingrese comando [buzzer ; rgb ; salir]:")
	func = input ("Ingrese funcion [prender ; apagar ; verde ; rojo ; azul]:")
	
    #Si escribo buzzer
	if  comando == 'buzzer':
		if func == 'prender':
			buzzer.on() #Buzzer se prende
		if func == 'apagar':
			buzzer.off() #Buzzer se apaga

    #Activo LED rgb
	if comando == 'rgb':
		if func == 'verde':
			verde.toggle() #Activo LED verde
		if func == 'rojo':
			rojo.toggle() #Activo LED rojo
		if func == 'azul':
			azul.toggle() #Activo LED azul

    #Si escribo salir que se termine el programa
	if comando == 'salir':
		break
