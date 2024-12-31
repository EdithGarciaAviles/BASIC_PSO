import random as rnd
import math 

# Función objetivo 1: Rosenbrock
# Mínimo en [1, 1, ..., 1] con valor 0
def funcion_rosenbrock(posicion):
    suma = 0
    for i in range(len(posicion) - 1):
        suma += 100 * (posicion[i + 1] - posicion[i]**2)**2 + (1 - posicion[i])**2
    return suma

# Función objetivo 3: Eggholder
# Global mínimo: f(x) = -959.6407 en x* = [512, 404.2319]
def funcion_eggholder(posicion):
    x1, x2 = posicion
    return (
        -(x2 + 47) * math.sin(math.sqrt(abs(x2 + x1 / 2 + 47)))
        - x1 * math.sin(math.sqrt(abs(x1 - (x2 + 47))))
    )

#Parámetros del PSO
num_particulas = 30
num_iteraciones = 1000
dimensiones = 2
limites = [(-512,512),(-512,512)] #Valores tuplados para cada dimension
c1 = 1.5  #Coeficiente cognitivo
c2 = 1.5  #Coeficiente social
W = 0.7   #Peso de Inercia

#Inicializar pocision y velocidad de las partículas
particulas = []
for i in range(num_particulas):
    d1 = rnd.uniform(limites[0][0],limites[0][1])
    d2 = rnd.uniform(limites[1][0],limites[1][1])
    posicion = [d1,d2]
    v1 = rnd.uniform(-1,1)
    v2 = rnd.uniform(-1,1)
    velocidad = [v1,v2]
    particulas.append(
        {'posicion':posicion,
         'velocidad':velocidad,
         'mejor_personal':posicion.copy(),
         'mejor_personal_valor':float('inf') }

    )
#Inicialización del mejor global
mejor_global = None
mejor_global_valor = float('inf')


#Estructurar el algoritmo
for i in range(num_iteraciones):
    for particula in particulas:
        #valor_actual = funcion_rosenbrock(particula['posicion'])
        valor_actual = funcion_eggholder(particula['posicion'])
        #Actualizar el mejor valor personal
        if valor_actual < particula['mejor_personal_valor']:
            particula['mejor_personal'] = particula['posicion'].copy()
            particula['mejor_personal_valor'] = valor_actual
        #Actualizar el mejor valor global
        if valor_actual < mejor_global_valor:
            mejor_global = particula['posicion'].copy()
            mejor_global_valor = valor_actual
    #Actualizacion del valor de las partículas
    for particula in particulas:
        for d in range(dimensiones):
            r1 = rnd.uniform(0,1) #Número aleatorio para c1
            r2 = rnd.uniform(0, 1)  # Número aleatorio para c2
            particula['velocidad'][d] = (
                W*particula['velocidad'][d] +
                c1*r1*(particula['mejor_personal'][d] - particula['posicion'][d]) +
                c2*r2*(mejor_global[d] - particula['posicion'][d])
            )
            #Actualizacion de la posicion de las particulas
            particula['posicion'][d] = particula['posicion'][d] + particula['velocidad'][d]

            #Asegurarse de que la posicion este dentro de los límites
            particula['posicion'][d] = max(limites[d][0], min(limites[d][1],particula['posicion'][d]))

    print(f'Iteración: {i+1}, Mejor global encontrado: {mejor_global}, valor: {mejor_global_valor}')




print('\n')
print(f'Mejor posición encontrada: {mejor_global}, Mejor valor encontrado: {mejor_global_valor}')



