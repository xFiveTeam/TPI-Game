import unittest
from unittest.mock import patch
from truco import jugar_truco, repartir_cartas, valor_carta, ganador_ronda, calcular_envido, valor_envido, solicitar_nombres_jugadores, CARTAS

class TestTruco(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        'Jugador1', 'Jugador2',  # Nombres de los jugadores
        '2', '1',  # Cantar envido y respuesta
        '1', '1', '1',  # Elegir cartas para Jugador1
        '1', '1', '1',  # Elegir cartas para Jugador2
        '1', '1',  # Cantar truco y respuesta
        '1', '1',  # Elegir cartas para Jugador1
        '1', '1',  # Elegir cartas para Jugador2
        '1', '1',  # Cantar truco y respuesta
        '1', '1',  # Elegir cartas para Jugador1
        '1', '1',  # Elegir cartas para Jugador2
        '1', '1',  # Cantar truco y respuesta
        '1', '1',  # Elegir cartas para Jugador1
        '1', '1',  # Elegir cartas para Jugador2
        '1', '1',  # Cantar truco y respuesta
        '1', '1',  # Elegir cartas para Jugador1
        '1', '1',  # Elegir cartas para Jugador2
    ])
    def test_jugar_truco(self, mock_input):
        # Llamar a la función que usa input
        jugar_truco()

    @patch('builtins.input', side_effect=['Jugador1', 'Jugador2'])
    def test_solicitar_nombres_jugadores(self, mock_input):
        jugador1, jugador2 = solicitar_nombres_jugadores()
        self.assertEqual(jugador1, 'Jugador1')
        self.assertEqual(jugador2, 'Jugador2')

    def test_repartir_cartas(self):
        mano1, mano2 = repartir_cartas()
        self.assertEqual(len(mano1), 3)
        self.assertEqual(len(mano2), 3)
        self.assertEqual(len(set(mano1 + mano2)), 6)  # Las cartas no deben repetirse

    def test_valor_carta(self):
        self.assertEqual(valor_carta(('1', 'Espada')), 14)
        self.assertEqual(valor_carta(('4', 'Copa')), 1)
        self.assertEqual(valor_carta(('7', 'Espada')), 12)

    def test_ganador_ronda(self):
        # Carta1 gana a Carta2
        self.assertEqual(ganador_ronda(('1', 'Espada'), ('7', 'Oro')), 1)
        # Carta2 gana a Carta1
        self.assertEqual(ganador_ronda(('4', 'Copa'), ('5', 'Espada')), 2)
        # Empate
        self.assertEqual(ganador_ronda(('3', 'Copa'), ('3', 'Espada')), 0)

    def test_calcular_envido(self):
        # Dos cartas del mismo palo
        mano = [('6', 'Espada'), ('5', 'Espada'), ('2', 'Oro')]
        self.assertEqual(calcular_envido(mano), 31)  # 20 + 6 + 5
        
        # Tres cartas diferentes
        mano = [('1', 'Espada'), ('3', 'Basto'), ('7', 'Oro')]
        self.assertEqual(calcular_envido(mano), 0)  # No hay cartas del mismo palo

        # Dos cartas altas del mismo palo
        mano = [('7', 'Espada'), ('2', 'Espada'), ('3', 'Oro')]
        self.assertEqual(calcular_envido(mano), 29)  # 20 + 7 + 2

    def test_valor_envido(self):
        self.assertEqual(valor_envido(('7', 'Espada')), 7)
        self.assertEqual(valor_envido(('10', 'Espada')), 0)  # Cartas mayores a 7 no suman
        self.assertEqual(valor_envido(('1', 'Oro')), 1)

if __name__ == '__main__':
    unittest.main()