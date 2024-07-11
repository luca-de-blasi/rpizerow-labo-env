import time
import ADS1x15
import math
from gpiozero import PWMLED

# Configura el ADC
ADS = ADS1x15.ADS1115(address=0x48, busnum=1)
ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()

# Pines GPIO para los LEDs
pin_led_azul = 26
pin_led_rojo = 19

# Crea objetos PWMLED para los LEDs
led_azul = PWMLED(pin_led_azul)
led_rojo = PWMLED(pin_led_rojo)

# Función para calcular la temperatura del termistor
def calcular_temperatura(valor_adc):
    tension = valor_adc * f
    resistencia = (tension * 10000) / (3.3 - tension)
    temperatura = 1 / (1 / (273.15 + 25) + (1 / 3950) * math.log(resistencia / 10000)) - 273.15
    return temperatura

while True:
    valor_pot = ADS.readADC(0) # Lee el valor del potenciómetro
    temperatura_deseada = 30 * valor_pot / 32767.5 # Escala el valor del potenciómetro a un rango de temperatura (0-30°C)
    valor_termistor = ADS.readADC(1) # Lee el valor del termistor
    temperatura_real = calcular_temperatura(valor_termistor)
    diferencia = temperatura_real - temperatura_deseada

    # Control proporcional
    if diferencia > 0:
        # Temperatura real mayor a la deseada: enciende LED azul
        brillo = min(abs(diferencia) / 5, 1)  # Brillo proporcional, máximo a 5°C
        led_azul.value = brillo
        led_rojo.off()
    elif diferencia < 0:
        # Temperatura real menor a la deseada: enciende LED rojo
        brillo = min(abs(diferencia) / 5, 1)
        led_rojo.value = brillo
        led_azul.off()
    else:
        # Temperaturas iguales: apaga ambos LEDs
        led_azul.off()
        led_rojo.off()

    print(f"Temperatura deseada: {temperatura_deseada:.2f}°C, Temperatura real: {temperatura_real:.2f}°C")

    time.sleep(0.2)
