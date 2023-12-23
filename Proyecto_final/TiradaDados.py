import random
import os

def limpiarpantalla():
    os.system('cls')

class Dados ():
    def __init__(self):
        self.caras_dado = [1,2,3,4,5,6]
        self.tiro_random = 0
    def tirar_dado(self):
        self.dado_tirado = random.choice(self.caras_dado)  
        pass
    def mostrar_dado(self):
        print(" El dado tirado es  :",self.dado_tirado)



op = True

while op:
    limpiarpantalla()

    print('   Tirada de Dados  ')
    print('====================')
    print('(1)----Jugar--------')
    print('(2)----Salir--------')
    print('====================')
    opcion = int(input('/n /n Seleccione una opción (1 o 2): '))
    
    if opcion == 1:
        print('Opción Jugar')
        dado1=Dados()
        dado1.tirar_dado()
        dado1.mostrar_dado()
        break
    elif opcion == 2:
        print('Opción Salir')
        op = False
    else:
        print('Opción no válida. Inténtelo de nuevo.')

print('Fin del programa')
