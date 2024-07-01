# primera versión de desplazamiento 
# scroll de texto (en la primera línea)
# versión: Julio-2024 (jt)
import machine
import i2c_lcd
import time
from machine import SoftI2C, Pin, I2C
from time import sleep
from i2c_lcd import I2cLcd

contador = 0
columnas = 20
col = 19

def scan(i2c):
    devices = i2c.scan()
    if len(devices) == 0:
        print("No i2c device !")
    else:
        print('i2c devices found:',len(devices))
    for device in devices:
        print("At address: ",hex(device))
    return devices

def try_LCD():
# inicializar la pantalla LCD
    global lcd
    sdaPIN = Pin(21)  #for ESP32
    sclPIN = Pin(22)

    i2c = SoftI2C(sda=sdaPIN, scl=sclPIN, freq=10000)
    devices = scan(i2c)
    if devices:
        display_id = scan(i2c)[0]
        totalRows = 4
        totalColumns = 20
        lcd = I2cLcd(i2c, display_id, totalRows, totalColumns)
        lcd.clear()

# Colocar un mensaje en una determinada
# posicion. línea 0-1-2-3 columna 0-20
# texto. (mensaje a mostrar)
# imprime_texto (se pasa el mensaje a desplazar)

def posicionar_texto(columna,linea,texto):
    lcd.move_to(columna,linea)
    lcd.putstr(texto)

def imprime_texto(text):
    lcd.move_to(col,0)
    lcd.putstr(text[indice:l])

# Función para desplazar el texto
# col=desplazar el texto por la columna 
# col=col-1 (condición col=0 y r<recorrer terminar 
# en textos largos); r=recorrer (inicializar valores)
# r - para determinar el recorrido del texto con
# recorrer.
# longitud=total caracteres del texto, que en la variable
# recorrer añadimos el total de columnas para saber el 
# recorrido exacto del texto.
#
def scroll_text(text):
    global col, longitud, indice, l, r, vueltas
    longitud=len(text)
    indice=0
    l=0
    vueltas=0
    recorrer=longitud+col

    while True:
        r=1
        l=0
        col=20
        vueltas=vueltas+1
  
        while r < recorrer:
            imprime_texto(text)            
            l=l+1
            col=col-1
            mensaje="                    " # limpiar linea
            posicionar_texto(0,0,mensaje)
            r=r+1

            while col==0 and r < recorrer:
               indice=indice+1
               imprime_texto(text)
               mensaje="                    " # limpiar linea
               posicionar_texto(0,0,mensaje)
               r=r+1
               l=l+1

        if r==recorrer:
            r=0
            indice=0
            col=20
            l=0
            mensaje="Deslizando ... "+str(vueltas)+" "
            posicionar_texto(0,3,mensaje)
            
while True:
    try_LCD()
    scroll_text("Peatones pasando a tope")

# scroll_text("mensaje a deslizar")
# es la función utilizada para desplazar el texto
