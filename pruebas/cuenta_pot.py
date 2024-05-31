#from picozero import Button, Pot
#Con from puedes usar directamente el comando importado "Button(15)"
#en lugar de "picozero.Button(15)"

import picozero
from time import sleep
#import time
import tm1637
from machine import Pin

#############################################
#DATOS DE CONEXIONES PARA EL DISPLAY TM1637
tm = tm1637.TM1637(clk=Pin(9), dio=Pin(4))
tm.brightness(4)
#############################################
button = picozero.Button(15)
pot = picozero.Pot(26)
button=Pin(15, Pin.IN, Pin.PULL_DOWN)

def display_counter(i):
    # Convierte el valor en una lista de dígitos
    tm.numbers(i // 60, i % 60, True)
    
def button_handler(pin): #control de la interrupción (evento pulsado o no)
    global running
    running = not running

button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
#crear un evento, para cuando se pulse el botón, crear la interrupción correspondiente


while True:
    t = int(pot.value*30)
    print(pot.value, t)
        
    if running:
        i = i - 1
        
       # if i > -1:
       if i > (t*60):
            i = 0
            
        display_counter(i)
        minutes = i // 60                   # How many full minutes left "Cociente entero de la división"
        seconds = i % 60                    # How many seconds left "Resto de la division"
        print (i, minutes, seconds)
        #write_potentiometer(counter % 256)  # Ajusta según tu potenciador
        time.sleep(1)  # Ajusta la velocidad del incremento del contador
        
    else:
        display_counter(i)
        time.sleep(0.1)


