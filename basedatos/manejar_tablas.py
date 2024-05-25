# -*- coding: utf-8 -*-
"""
Editor de Spyder
Epidural.xlsx es un archivo de Excel , hay que comprobar según la tabla que se indique
Este es un archivo temporal.
"""
# cargar la base de datos 
import pandas as pd
datos = pd.read_excel("Epidural.xlsx")

# visualizar el nombre de las variables
print (datos.columns)

# datos estadísticos descriptivos
print (datos[["edad"]].describe)

# filtramos a las mujeres que recibieron epidural
# epidural = 1 (guardar en epidural_si)
epidural_si = datos.loc[datos["EPIDURAL"] == 1]

# variable "edad" 3 categorias
# a (<25 años) por debajo
# b (=25 años) igual
# c (> 25 años) por encima

# realizamos la recodificación de la variable edad
# según los datos anteriores
# rangos - utilizar la función "bins" 
# - utilizar "-float (numeros negativos)
# o           "float (infinito  negativo o positivo posible
# crear tabla de frecuencias (frequency_table) (serie)
# 
datos["edad_categorias"] = pd.cut(datos['edad'], bins=[-float('inf'), 24, 25, float('inf')], labels=['DEBAJO', 'IGUAL', 'ENCIMA'])
frequency_table = datos['edad_categorias'].value_counts()                                                      

# media de temperatura (temp1 y temp2), en variable media 
media = datos[['TEMP1', 'TEMP2']].mean(axis=1)
datos['TEMP_MEDIA'] = media

