import os

def mover_cursor(fila, columna):
    print(f"\033[{fila};{columna}H", end="")

def limpiar_pantalla():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix/Linux/MacOS/BSD/etc.
    else:
        os.system('clear')

def mostrar_menu():
    limpiar_pantalla()
    mover_cursor(1, 1)
    print("Menú:")
    mover_cursor(2, 1)
    print("1. Opción 1")
    mover_cursor(3, 1)
    print("2. Opción 2")
    mover_cursor(4, 1)
    print("3. Opción 3")
    mover_cursor(5, 1)
    print("4. Salir")

def opcion1():
    mover_cursor(7, 1)
    print("Has seleccionado la Opción 1.")

def opcion2():
    mover_cursor(7, 1)
    print("Has seleccionado la Opción 2.")

def opcion3():
    mover_cursor(7, 1)
    print("Has seleccionado la Opción 3.")

def main():
    while True:
        mostrar_menu()
        mover_cursor(6, 1)
        opcion = input("Selecciona una opción: ")

        limpiar_pantalla()
        mostrar_menu()
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            mover_cursor(7, 1)
            print("Saliendo del programa...")
            break
        else:
            mover_cursor(7, 1)
            print("Opción no válida, por favor selecciona una opción válida.")
        
        mover_cursor(8, 1)
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
