from gpiozero import LED, Button
from time import sleep

#Defino los leds con los pines
led.verde = led (13)
led.rojo = led (19)
led.azul = led (26)

while True:

	#Apago todos los leds
	led.rojo.off()
	led.verde.off()
	led.azul.off()

	#Prendo el led rojo por 1 segundo
	led.rojo.on()
	sleep(1)

	#Prendo el led azul por 0,5 segundos
	led.azul.on()
	sleep(0.5)

	#Prendo el led verde por 0.25 segundos
	led.verde.on()
	sleep(0.25)
