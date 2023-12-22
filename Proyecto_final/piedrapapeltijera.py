import random
import os

op = True

class Jugador():
    
    def __init__(self):
        self.nombre = 'nombre'
        self.puntos = 0
        self.eleccion = '-'

    def colocar_nombre(self):
        self.nombre = input('Ingrese nombre : ')
        limpiarpantalla()

    def elegir(self):
        print('|1| Piedra')
        print('|2| Papel')
        print('|3| Tijera')
        opcion = int(input('Ingrese eleccion : '))
        if opcion == 1:
            self.eleccion = 'Piedra'
        elif opcion == 2:
            self.eleccion = 'Papel'
        elif opcion == 3:
            self.eleccion = 'Tijera'
        limpiarpantalla()
        return self.eleccion


class JugadorIA():

    def __init__(self):
        self.nombre = 'Inteligencia Artificial'
        self.eleccion = ''

    def jugar(self):
        opciones = ["Piedra", "Papel", "Tijera"]
        self.eleccion = random.choice(opciones)  

def limpiarpantalla():
    os.system('cls')

def determinar_ganador(player1, IA):
    
    if player1.eleccion == IA.eleccion:
        return "Empate"
    elif (player1.eleccion == "Piedra" and IA.eleccion == "Tijera") or \
         (player1.eleccion == "Papel" and IA.eleccion == "Piedra") or \
         (player1.eleccion == "Tijera" and IA.eleccion == "Papel"):
        return "Ganaste"
    else:
        return "Perdiste"       
    

def jugar():                            
    player1 = Jugador()
    IA = JugadorIA()
    player1.colocar_nombre()
    
    for _ in range(3):  # Jugar tres veces
        player1.elegir()
        IA.jugar()
        print(f'{player1.nombre} eligió: {player1.eleccion}')
        print(f'{IA.nombre} eligió: {IA.eleccion}')
        
        resultado = determinar_ganador(player1, IA)
        print(f'Resultado de la ronda: {resultado}')

while op:
    print('   Menu del juego   ')
    print('====================')
    print('(1)----Jugar--------')
    print('(2)----Salir--------')
    opcion = int(input('Seleccione una opción (1 o 2): '))
    limpiarpantalla()
    if opcion == 1:
        print('Opción Jugar')
        jugar()

    elif opcion == 2:
        print('Opción Salir')
        op = False
    else:
        print('Opción no válida. Inténtelo de nuevo.')

print('Fin del programa')
