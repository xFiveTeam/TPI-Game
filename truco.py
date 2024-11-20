import random

# Definimos las cartas y sus valores según el Truco Argentino
CARTAS = [
    ('1', 'Espada'), ('1', 'Basto'), ('7', 'Espada'), ('7', 'Oro'),
    ('3', 'Espada'), ('3', 'Basto'), ('3', 'Copa'), ('3', 'Oro'),
    ('2', 'Espada'), ('2', 'Basto'), ('2', 'Copa'), ('2', 'Oro'),
    ('1', 'Copa'), ('1', 'Oro'), ('12', 'Espada'), ('12', 'Basto'),
    ('12', 'Copa'), ('12', 'Oro'), ('11', 'Espada'), ('11', 'Basto'),
    ('11', 'Copa'), ('11', 'Oro'), ('10', 'Espada'), ('10', 'Basto'),
    ('10', 'Copa'), ('10', 'Oro'), ('7', 'Basto'), ('7', 'Copa'),
    ('6', 'Espada'), ('6', 'Basto'), ('6', 'Copa'), ('6', 'Oro'),
    ('5', 'Espada'), ('5', 'Basto'), ('5', 'Copa'), ('5', 'Oro'),
    ('4', 'Espada'), ('4', 'Basto'), ('4', 'Copa'), ('4', 'Oro')
]

VALORES = {
    ('1', 'Espada'): 14, ('1', 'Basto'): 13, ('7', 'Espada'): 12, ('7', 'Oro'): 11,
    ('3', 'Espada'): 10, ('3', 'Basto'): 10, ('3', 'Copa'): 10, ('3', 'Oro'): 10,
    ('2', 'Espada'): 9, ('2', 'Basto'): 9, ('2', 'Copa'): 9, ('2', 'Oro'): 9,
    ('1', 'Copa'): 8, ('1', 'Oro'): 8, ('12', 'Espada'): 7, ('12', 'Basto'): 7,
    ('12', 'Copa'): 7, ('12', 'Oro'): 7, ('11', 'Espada'): 6, ('11', 'Basto'): 6,
    ('11', 'Copa'): 6, ('11', 'Oro'): 6, ('10', 'Espada'): 5, ('10', 'Basto'): 5,
    ('10', 'Copa'): 5, ('10', 'Oro'): 5, ('7', 'Basto'): 4, ('7', 'Copa'): 4,
    ('6', 'Espada'): 3, ('6', 'Basto'): 3, ('6', 'Copa'): 3, ('6', 'Oro'): 3,
    ('5', 'Espada'): 2, ('5', 'Basto'): 2, ('5', 'Copa'): 2, ('5', 'Oro'): 2,
    ('4', 'Espada'): 1, ('4', 'Basto'): 1, ('4', 'Copa'): 1, ('4', 'Oro'): 1
}

# Función para repartir cartas
def repartir_cartas():
    random.shuffle(CARTAS)
    return CARTAS[:3], CARTAS[3:6]

# Función para calcular el valor de una carta
def valor_carta(carta):
    return VALORES[carta]

# Función para determinar el ganador de una ronda
def ganador_ronda(carta1, carta2):
    if valor_carta(carta1) > valor_carta(carta2):
        return 1
    elif valor_carta(carta1) < valor_carta(carta2):
        return 2
    else:
        return 0

# Función para calcular los puntos del envido
def calcular_envido(mano):
    envido = 0
    for i in range(len(mano)):
        for j in range(i + 1, len(mano)):
            if mano[i][1] == mano[j][1]:  # Mismo palo
                puntos = 20 + valor_envido(mano[i]) + valor_envido(mano[j])
                envido = max(envido, puntos)
    return envido

# Función para calcular el valor del envido de una carta
def valor_envido(carta):
    valor = int(carta[0])
    return valor if valor <= 7 else 0

# Función para que un jugador elija una carta
def elegir_carta(mano, jugador):
    print(f"Mano de {jugador}: {mano}")
    while True:
        opciones = [str(i+1) for i in range(len(mano))]
        eleccion = input(f"{jugador}, elige una carta ({', '.join(opciones)}): ")
        if eleccion in opciones:
            return mano.pop(int(eleccion) - 1)
        else:
            print("Elección inválida. Intenta de nuevo.")

# Función para manejar los cantos del truco
def cantar_truco(jugador):
    opciones = ["1", "2", "3", "4"]
    print(f"{jugador}, ¿quieres cantar Truco? (1: No, 2: Truco, 3: Retruco, 4: Vale Cuatro)")
    eleccion = input(f"Elige una opción ({', '.join(opciones)}): ")
    if eleccion in opciones:
        return int(eleccion)
    else:
        print("Elección inválida. Intenta de nuevo.")
        return cantar_truco(jugador)

# Función para manejar la respuesta al truco
def responder_truco(jugador):
    opciones = ["1", "2", "3", "4"]
    print(f"{jugador}, ¿quieres aceptar el Truco? (1: No, 2: Sí, 3: Retruco, 4: Vale Cuatro)")
    eleccion = input(f"Elige una opción ({', '.join(opciones)}): ")
    if eleccion in opciones:
        return int(eleccion)
    else:
        print("Elección inválida. Intenta de nuevo.")
        return responder_truco(jugador)

# Función para manejar los cantos del envido
def cantar_envido(jugador):
    opciones = ["1", "2", "3", "4"]
    print(f"{jugador}, ¿quieres cantar Envido? (1: No, 2: Envido, 3: Real Envido, 4: Falta Envido)")
    eleccion = input(f"Elige una opción ({', '.join(opciones)}): ")
    if eleccion in opciones:
        return int(eleccion)
    else:
        print("Elección inválida. Intenta de nuevo.")
        return cantar_envido(jugador)

# Función para manejar la respuesta al envido
def responder_envido(jugador):
    opciones = ["1", "2", "3", "4"]
    print(f"{jugador}, ¿quieres aceptar el envido? (1: No, 2: Sí, 3: Real Envido, 4: Falta Envido)")
    eleccion = input(f"Elige una opción ({', '.join(opciones)}): ")
    if eleccion in opciones:
        return int(eleccion)
    else:
        print("Elección inválida. Intenta de nuevo.")
        return responder_envido(jugador)

# Función para solicitar los nombres de los jugadores
def solicitar_nombres_jugadores():
    jugador1 = input("Ingrese el nombre del Jugador 1: ")
    jugador2 = input("Ingrese el nombre del Jugador 2: ")
    return jugador1, jugador2

# Función principal del juego
def jugar_truco():
    jugador1, jugador2 = solicitar_nombres_jugadores()

    mano1, mano2 = repartir_cartas()
    puntos_ronda_jugador1 = 0
    puntos_ronda_jugador2 = 0
    cartas_jugadas = []

    # Mostrar las cartas de cada jugador
    print(f"Cartas de {jugador1}: {mano1}")
    print(f"Cartas de {jugador2}: {mano2}")

    # Cantar envido
    envido = 0
    envido_puntos = 0
    envido = cantar_envido(jugador1)
    if envido == 1:
        envido = cantar_envido(jugador2)
    if envido != 1:
        respuesta = responder_envido(jugador1 if envido == 2 else jugador2)
        if respuesta == 1:
            print("Envido no aceptado")
            envido_puntos = 2
        elif respuesta == 2:
            envido_puntos = 2
        elif respuesta == 3:
            envido_puntos = 5
            respuesta = responder_envido(jugador2 if envido == 2 else jugador1)
            if respuesta == 1:
                print("Real Envido no aceptado")
                envido_puntos = 5
            elif respuesta == 4:
                envido_puntos = 15
                respuesta = responder_envido(jugador1 if envido == 2 else jugador2)
                if respuesta == 1:
                    print("Falta Envido no aceptado")
                    envido_puntos = 15
                else:
                    envido_jugador1 = calcular_envido(mano1)
                    envido_jugador2 = calcular_envido(mano2)
                    if envido_jugador1 > envido_jugador2:
                        print(f"{jugador1} gana la falta envido")
                    elif envido_jugador2 > envido_jugador1:
                        print(f"{jugador2} gana la falta envido")
                    else:
                        print("Empate en la falta envido")
                    return
        else:
            envido_jugador1 = calcular_envido(mano1)
            envido_jugador2 = calcular_envido(mano2)
            if envido_jugador1 > envido_jugador2:
                print(f"{jugador1} gana el envido")
            elif envido_jugador2 > envido_jugador1:
                print(f"{jugador2} gana el envido")
            else:
                print("Empate en el envido")

    # Jugar las manos y cantar truco
    truco = 1
    for i in range(3):
        carta_jugador1 = elegir_carta(mano1, jugador1)
        carta_jugador2 = elegir_carta(mano2, jugador2)

        cartas_jugadas.append((carta_jugador1, carta_jugador2))
        resultado = ganador_ronda(carta_jugador1, carta_jugador2)
        if resultado == 1:
            puntos_ronda_jugador1 += 1
        elif resultado == 2:
            puntos_ronda_jugador2 += 1

        print(f"Cartas jugadas hasta ahora:")
        for j, (carta1, carta2) in enumerate(cartas_jugadas):
            print(f"Ronda {j+1}: {jugador1} jugó {carta1}, {jugador2} jugó {carta2}")

        # Preguntar si los jugadores quieren cantar truco
        if truco == 1:
            truco = cantar_truco(jugador1)
            if truco == 1:
                truco = cantar_truco(jugador2)
            if truco != 1:
                respuesta_truco = responder_truco(jugador1 if truco == 2 else jugador2)
                if respuesta_truco == 1:
                    print("Truco no aceptado")
                    break
                truco = respuesta_truco

    if puntos_ronda_jugador1 > puntos_ronda_jugador2:
        print(f"{jugador1} gana la ronda")
    elif puntos_ronda_jugador2 > puntos_ronda_jugador1:
        print(f"{jugador2} gana la ronda")
    else:
        print("Empate en la ronda")

# Ejecutar el juego
if __name__ == '__main__':
    jugar_truco()