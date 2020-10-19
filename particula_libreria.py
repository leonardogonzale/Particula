from particula import Particula

class Particula_libreria:
    def __init__(self):
        self.__particulas =[]

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)    

    def agregar_inicio(self, particula:Particula):
         self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)    

l01 = Particula(origen_x=3, origen_y=5, destino_x=5, destino_y=9, velocidad=45, red=123, green=456, blue=789, distancia=0)
l02 = Particula(3, 5, 5, 9, 45, 123, 456, 789, 0)
particula_libreria = Particula_libreria()
particula_libreria.agregar_final(l01)
particula_libreria.agregar_inicio(l02)
particula_libreria.agregar_inicio(101)
particula_libreria.mostrar()
