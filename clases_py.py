# -*- coding: utf-8 -*-
"""clases.py
 Programación de creación de clases (orientado a ojetos)
 definir la clase "Clase" . objeto (imprimir y datos)
Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CdJ7Pw1G-d_qBt4w4ZjZoNEHver4bBf7
"""

#CLASES
class Clase:
   def _init_ (self, numero, palabra):
       self.numero = numero
       self.palabra = palabra
       self.a = numero**2
       self.b = numero**3
       self.c = 999
   def imprimir(self):
       pal = self.palabra
       return pal
   def datos(self):
       num = self.numero
       a = self.a
       b = self.b
       c = self.c
       return datos

#a=Clase(8, "Juan")
Clase.imprimir="Juan"
print(Clase.imprimir)
#a.dime_datos(self)
Clase.datos.num=80
Clase.datos.a=1
print(Clase.datos.num)
print(Clase.datos.a)
