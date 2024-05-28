# un único bucle (contador abajo / arriba) base: chatgpt
import time
# Establecemos los valores iniciales
inicio = 9
fin = 1
cuenta_atras = False  # Variable para controlar la dirección de la cuenta

# Inicializamos el contador con el valor de 'inicio'
contador = inicio

# Bucle while único para realizar la cuenta atrás y adelante
while True:
    # Comprobamos si estamos en la cuenta atrás
    
    if cuenta_atras:
        contador -= 1  # Decrementamos el contador
        if contador < fin:
            cuenta_atras = False  # Cambiamos la dirección de la cuenta
            if contador==0:
                print("** Hacia delante **")
    else:
        contador += 1  # Incrementamos el contador
                
        if contador > inicio:
            cuenta_atras = True
            if contador==10:
                print("** Hacia atrás **")

    print(contador)
    time.sleep(0.10)
