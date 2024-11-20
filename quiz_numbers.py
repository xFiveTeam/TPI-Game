print("¡Bienvenido al Quiz Matemático!")
print("Responde correctamente a las siguientes preguntas para ganar puntos.")
print("Escribe 'salir' en cualquier momento para terminar el juego.\n")

puntos = 0

# Pregunta 1
print("Pregunta 1: ¿Cuánto es 5 + 3?")
respuesta = input("Tu respuesta: ")

if respuesta.lower() == "salir":
    print("Gracias por jugar. ¡Hasta pronto!")
else:
    if respuesta == "8":
        print("¡Correcto!")
        puntos += 1
    else:
        print("Incorrecto. La respuesta correcta es 8.")

# Pregunta 2
print("\nPregunta 2: ¿Cuánto es 9 - 4?")
respuesta = input("Tu respuesta: ")

if respuesta.lower() == "salir":
    print("Gracias por jugar. ¡Hasta pronto!")
else:
    if respuesta == "5":
        print("¡Correcto!")
        puntos += 1
    else:
        print("Incorrecto. La respuesta correcta es 5.")

# Pregunta 3
print("\nPregunta 3: ¿Cuánto es 6 * 2?")
respuesta = input("Tu respuesta: ")

if respuesta.lower() == "salir":
    print("Gracias por jugar. ¡Hasta pronto!")
else:
    if respuesta == "12":
        print("¡Correcto!")
        puntos += 1
    else:
        print("Incorrecto. La respuesta correcta es 12.")

# Pregunta 4
print("\nPregunta 4: ¿Cuánto es 10 / 2?")
respuesta = input("Tu respuesta: ")

if respuesta.lower() == "salir":
    print("Gracias por jugar. ¡Hasta pronto!")
else:
    if respuesta == "5":
        print("¡Correcto!")
        puntos += 1
    else:
        print("Incorrecto. La respuesta correcta es 5.")

# Resultado final
print("\nJuego terminado.")
print(f"Tu puntaje final es: {puntos}/4.")
if puntos == 4:
    print("¡Excelente! Eres un genio matemático.")
elif puntos >= 2:
    print("¡Buen trabajo! Pero aún puedes mejorar.")
else:
    print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")