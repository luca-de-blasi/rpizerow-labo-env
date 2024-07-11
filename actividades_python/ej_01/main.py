from gpiozero import LED, Button
from signal import pause

led = LED(26)
boton = Button(18)

boton.when_pressed = led.on
boton.when_released = led.off

pause()
