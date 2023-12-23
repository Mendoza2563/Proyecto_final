import random

class NumeroRandom:
    def __init__(self):
        self.numero_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.numero_aleatorio = random.choice(self.numero_array)

class Jugador:
    def __init__(self):
        self.numero_elegido = 0

class ComputadoraIA:
    def __init__(self):
        super().__init__()

def Logica(jugador, computadora_IA, numerorandom):
    
    while True:
        # Turno del jugador
        jugador.numero_elegido = int(input("Adivina el número (1-9): "))
        if jugador.numero_elegido == numerorandom.numero_aleatorio:
            print("¡Felicidades! Has adivinado el número.")
            break
        else:
            print("Número incorrecto. ¡Inténtalo de nuevo!")

        # Turno de la computadora
        computadora_IA.numero_elegido = random.choice(numerorandom.numero_array)
        print(f"La computadora elige: {computadora_IA.numero_elegido}")
        if computadora_IA.numero_elegido == numerorandom.numero_aleatorio:
            print("La computadora ha adivinado el número.")
            break
        else:
            print("La computadora no ha adivinado el número. Sigue intentando.")

# Crear instancias de las clases
numero_random = NumeroRandom()
jugador = Jugador()
computadora = ComputadoraIA()

# Llamar a la función de lógica del juego
Logica(jugador, computadora, numero_random)


    





