from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self,  origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0, distancia=0):
        self.__origen_x = origen_x 
        self.__origen_y = origen_y 
        self.__destino_x = destino_x 
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)

    def __str__(self):
       return (
           'Origen_x: ' + str(self.__origen_x) + '\n' + 
           'Origen_y: ' + str(self.__origen_y) + '\n' + 
           'Destino_x: ' + str(self.__destino_x) + '\n' + 
           'Destino_y: ' + str(self.__destino_y) + '\n' + 
           'Velocidad: ' + str(self.__velocidad) + '\n' + 
           'Red: ' + str(self.__red) + '\n' + 
           'Green ' + str(self.__green) + '\n' + 
           'Blue ' + str(self.__blue) + '\n' + 
           'Distancia ' + str(self.__distancia) + '\n' )     

#l01 = Particula(origen_x=3, origen_y=5, destino_x=5, destino_y=9, velocidad=45, red=123, green=456, blue=789, distancia=0)
#print(l01)
#l02 = Particula(3, 5, 5, 9, 45, 123, 456, 789, 0)
#print(l02)