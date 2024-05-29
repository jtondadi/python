import RPi.GPIO as GPIO
import time
from machine import Pin

PIN=22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT) #¡Ojo!, 1-wire OFF para que no dé problemas
button=Pin(15, Pin.IN, Pin.PULL_DOWN)

from tkinter import *

root=Tk()
root.title("CONTROL ON OFF")

miframe=Frame(root, width=350,height=400, bg="Blue")
miframe.pack()

def button_handler(pin):
    global running
    running = not running

def codigoBotonON():
    GPIO.output(PIN,True)

def codigoBotonOFF():
    GPIO.output(PIN,False)

def codigoBotonFLASH():
    for i in range(1,10):
        GPIO.output(PIN,False)
        time.sleep(0.1)
        GPIO.output(PIN,True)
        time.sleep(0.1)

botonON=Button(miframe, bg="green", text="ON", command=codigoBotonON)
botonON.place(x=100, y=100)

botonOFF=Button(miframe, bg="orange", text="OFF", command=codigoBotonOFF)
botonOFF.place(x=200, y=100)

botonFLASH=Button(miframe, bg="yellow", text="FLASHING", command=codigoBotonFLASH)
botonFLASH.place(x=130, y=200)

button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

root.mainloop()
