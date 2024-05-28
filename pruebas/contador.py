# Establecemos los valores iniciales
inicio = 10
fin = 0
cuenta_atras = True  # Variable para controlar la dirección de la cuenta

# Inicializamos el contador con el valor de 'inicio'
contador = inicio

# Bucle while único para realizar la cuenta atrás y adelante
while True:
    print(contador)

    # Comprobamos si estamos en la cuenta atrás
    if cuenta_atras:
        contador -= 1  # Decrementamos el contador
        if contador < fin:
            cuenta_atras = False  # Cambiamos la dirección de la cuenta
    else:
        contador += 1  # Incrementamos el contador
        if contador > inicio:
            break  # Salimos del bucle cuando alcanzamos el valor de 'inicio' de nuevo

