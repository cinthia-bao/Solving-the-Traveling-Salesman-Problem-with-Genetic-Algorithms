import random
from prettytable import PrettyTable # verlos
import csv # archivo
import json

individuos = 10  # Tamaño de la población
digitos = 18  # Longitud de cada individuo

with open('matriz_distancias.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    matriz = [row for row in reader]

def initialize_population(tamano, digitos):
    population = set()  # Para evitar duplicados en la población
    while len(population) < tamano:
        individuo = random.sample(range(1,19), digitos)   # Genera un individuo sin repetición
        population.add(tuple(individuo))  # Convertir a tupla para que se pueda agregar al set
    return [list(ind) for ind in population]  # Convertir de nuevo a listas

def aptitud_calculate(population):
    distancias = []
    for i in range(len(population)):
        individuo = population[i]
        distancia =0
        for j in range(len(individuo)):
            ciudad1 = individuo[j-1]
            ciudad2 = individuo[j]
            r = float(matriz[ciudad1][ciudad2])
            distancia +=  r
        distancias.append(distancia) 
    sorted_data = sorted(zip(distancias, population), reverse=False, key=lambda x:x[0])
    sorted_distance, sorted_population = zip(*sorted_data)
    sorted_distance, sorted_population = list(sorted_distance), list(sorted_population)
    
    # NORMALIZANDO DE 0 1
    sorted_aptitude = [round(sorted_distance[0]/float(num), 6)for num in sorted_distance]

    return sorted_population, sorted_aptitude, sorted_distance

population100 = initialize_population(100, digitos)
population200 = initialize_population(200, digitos)
population500 = initialize_population(500, digitos)
population1000 = initialize_population(1000, digitos)

spob100, apt, sdis = aptitud_calculate(population100)
spob200, apt, sdis = aptitud_calculate(population200)
spob500, apt, sdis = aptitud_calculate(population500)
spob1000, apt, sdis = aptitud_calculate(population1000)

poblaciones = {
        'poblacion100': spob100,
        'poblacion200': spob200,
        'poblacion500': spob500,
        'poblacion1000': spob1000
        }

with open('poblaciones.json', 'w') as f:
    json.dump(poblaciones, f, indent=4)

print("✅ Poblaciones guardadas en 'poblaciones.json'")






