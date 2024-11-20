import os

def mostrar_menu():
    print("Menú Principal")
    print("1. Jugar al Truco")
    print("2. Jugar al Quiz de Números")
    print("3. Salir")

def ejecutar_truco():
    os.system('python truco.py')

def ejecutar_quiz_numbers():
    os.system('python quiz_numbers.py')

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ")
        if opcion == '1':
            ejecutar_truco()
        elif opcion == '2':
            ejecutar_quiz_numbers()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == '__main__':
    main()