# 1. CREAR VARIABLES
print("Actividad 1. CREAR VARIABLES")
# Crea la variable ahorros
ahorros = 100
# Print out ahorros
print(ahorros)

# 2. CALCULAR CON VARIABLES
print("Actividad 2. CALCULAR VARIABLES")
# Crea la variable ahorros
ahorros = 100
# Crea la variable growth_multiplier
growth_multiplier = 1.1
# Calcula la variable result
result = ahorros * growth_multiplier ** 7
# Print out result
print(result)

# 3. CREAR BOOLEANOS
print("Actividad 3. BOOLEANOS")
# Crea la variable desc
desc = "compound interest"
# Crea la variable profitable
profitable = True
print(profitable)

# 4. CONVERTIR VARIABLES
print("Actividad 4. CONVERSIÓN DE VARIABLES")
#Definir las variables ahorros and resultado
ahorros = 100
resultado = 100 * 1.10 ** 7
# Establece el printout
print("Empecé con €" + str(ahorros) + " y ahora tengo €" + str(resultado) + ". ¡Increíble!")
# Definition of pi_string
pi_string = "3.1415926"
# Convertir pi_string en una variable float: pi_float
pi_float = float(pi_string)

#5.LISTAS
print("Actividad 5. LISTAS")
# variables De las áreas de la casa (en metros cuadrados)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# Crea una lista llamada areas
areas = [hall, kit, liv, bed, bath]
# Imprime areas
print(areas)

#6. LISTAS CON DIFERENTES TIPOS DE DATOS
print("Actividad 6. TIPOS DE DATOS")
# variables de las áreas de la casa (en metros cuadrados)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# Adapta la lista areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]
# Print areas
print(areas)

#7. USO DE ÍNDICES
print("Actividad 7. INDICES")
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Print out second element from areas
print(areas[1])
# Print out last element from areas
print(areas[-1])
# Print out the area of the living room
print(areas[5])

#8. CÁLCULO CON LISTAS
print("Actividad 8. LISTAS")
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]
# Print the variable eat_sleep_area
print(eat_sleep_area)

#9. REBANAR LISTAS
print("Actividad 9. Rebanar Listas")
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Use slicing to create downstairs
downstairs = areas[0:6]
# Use slicing to create upstairs
upstairs = areas[6:10]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

#10. SUSTITUIR ELEMENTOS
print("Actividad 10. Sustituir elementos")
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Correct the bathroom area
areas[-1] = 10.50
# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)

#11. AMPLIAR LISTA
print("Actividad 11. Ampliar lista")
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]
#Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
print(areas_1)
print(areas_2)

#12. CAMBIOS EN LISTAS
print("Actividad 12. Cambios en lista")
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
areas_copy = list (areas)
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)

#13. COMPARTIVA DE IGUALDAD
print("Actividad 13. Comparativa")
# Comparación de booleans
print(True == False)
# Comparación de integers
print(-5 * 15 != 75)
# Comparación de strings
print("pyscript" == "PyScript")
# Comparación de boolean con integer
print(True == 1)

#14. AND, OR, NOT
print("Actividad 14. And, or y Not")
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0
# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)
# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)
# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)

#15. IF
print("Actividad 15. IF")
area = 10.0
if(area < 9) :
   print("small")
elif(area < 12) :
   print("medium")
else :
   print("large")

#16. WHILE TRUE (case) útil para menús
# Mientras no seleccione 0 [básico --- salta en la misma línea]
while True:
    opcion=int(input("Opcion: 0. Salir; 1. On; 2. Off"))
    
    match opcion:
        case 1:
            print("1. encendido")
        case 2:
            print("2. apagado")
        case 0:
            print("saliendo")
            break

#17 A a Z
#ord (conversión de cadena a número)
empezar=ord('a')
fin=ord('z')+1

i=empezar
while i != empezar:
         caracter=chr(i)
         i=i+1
         print("caracter",caracter)

#18 (cuenta atrás)
for i in range(100,0,-1):
         print(i)



