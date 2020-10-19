from math import sqrt 

def distancia_euclidiana(origen_x, origen_y, destino_x, destino_y):
    return sqrt((destino_x - origen_x)**2 + (destino_y - origen_y)**2)


origen_x = (3)
destino_x = (5)
origen_y = (5)
destino_y = (9)

print(distancia_euclidiana(origen_x, origen_y, destino_x, destino_y))