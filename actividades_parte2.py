# -*- coding: utf-8 -*-
"""ACTIVIDADES_parte2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RM_DUsNM9EQSeSN5BI2BJEsTixhuxIvN
"""

# 1. FUNCIONES FAMILIARES
print("Actividad 1. Funciones familiares")
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True
# Print out type of var1
print(type(var1))
# Print out length of var1
print(len(var1))
# Convert var2 to an integer: out2
out2 = int(var2)

# 2. MÉTODOS ASOCIADOS A STRING
print("Actividad 2. Método de asociación al string")
# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))

# 3. LISTAS (I)
print("Actividad 3. LISTAS (I)")
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
print(areas.index(20.0))
# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# 4. LISTAS (II)
print("Actividad 4. CONVERSIÓN DE VARIABLES")
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

#5. NUMPY (array)
print("Actividad 5. NUMPY (array)")
# Import the numpy package as np
import numpy as np
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out type of np_baseball
print(type(np_baseball))

#6. BUCLE WHILE
print("Actividad 6. BUCLE WHILE")
x = 1
while x < 4 :
  print(x)
  x = x + 1

#7. BUCLE WHILE (offset)
print("Actividad 7. BUCLE WHILE")
# Initialize offset
offset = 8
# Code the while loop
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)

#8. FOR
print("Actividad 8. FOR")
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for area in areas :
    print(area)

#9. FOR (II)
print("Actividad 9. For (II)")
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))

#10. SUSTITUIR ELEMENTOS
print("Actividad 10. Sustituir elementos")
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Correct the bathroom area
areas[-1] = 10.50
# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)

#11. IMPORTAR PAQUETES (math)
print("Actividad 11. Importar paquetes")
# Import the math package
import math
# Definition of radius
r = 0.43
# Calculate C
C = 2 * r * math.pi
# Calculate A
A = math.pi * r ** 2
# Build printout
print("Circunferencia: " + str(C))
print("Area: " + str(A))