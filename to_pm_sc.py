################################################################
#   Cinthia Alejandra Olvera Bautista           marzo - 2025
#
#   *SELECCION:         TOURNAMENT
#   *CRUZA:             PMX       
#   *MUTACION:          SCRAMBLE 
#   *TERMINO:           DELTA     
################################################################
#   Delta ya se llegó al optimo si:
#               tolerancia = aptitud_mejor - aptitud_promedio
#   ya no se encuentran mejores individuos

tolerancia = .05
name = 'Generaciones_to_pm_sc.json'
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
# Para configuracion de resultados
from  config_results import *
# Para calcular la aptitud
from get_poblation import aptitud_calculate
# Importar metodos
from metodos_seleccion import tournament
from metodos_cruza import PMX
from metodos_mutacion import scramble 
from metodos_elitismo import elitismo

# Cargar el archivo JSON
with open('poblaciones.json', 'r') as file:
    data = json.load(file)

# Se aceptan argumentos para indicar la poblacion
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python to_pm_sc.py <número>")
        sys.exit(1)
    numero = sys.argv[1]
    ruta_carpeta_poblacion = f'Poblacion{numero}'
    crear_carpeta_si_no_existe(ruta_carpeta_poblacion)
    
    ruta_carpeta = 'To_pm_sc'
    ruta_carpeta=os.path.join(ruta_carpeta_poblacion,ruta_carpeta)
    crear_carpeta_si_no_existe(ruta_carpeta)
    poblacion_100 = data.get(f"poblacion{numero}", [])
    print(ruta_carpeta)

def evolucion(poblacion, tolerancia,ruta):
    i=0
    numero = len(poblacion)
    delta_ap=tolerancia*2
    poblacion, aptitud, distance=aptitud_calculate(poblacion_100)
    guardar_poblacion_generaciones(i, poblacion, name, ruta)
    while tolerancia < delta_ap:
        # Seleccion
        padres1, padres2 = tournament(poblacion,int(numero/2))
        # Cruza
        hijo1, hijo2 = PMX(padres1, padres2)
        poblacion = padres1+padres2+hijo1+hijo2
        poblacion, aptitud, distance = aptitud_calculate(poblacion)
        # Mutacion
        poblacion = scramble(poblacion[:int(numero)], 5*2)
        poblacion, aptitud, distance = aptitud_calculate(poblacion)
        poblacion, aptitud = elitismo(poblacion,aptitud,int(numero))
        prom_ap = np.mean(aptitud)
        delta_ap = aptitud[0]-prom_ap 
        i+=1
    
        guardar_poblacion_generaciones(i, poblacion, name,ruta)


evolucion(poblacion_100,tolerancia,ruta_carpeta) 

# RESULTADOS 
generaciones = leer_json(f'{ruta_carpeta}/{name}')

distancias_minimas, distancias,mejor_individuo, mejor_distancia = guardar_distancias(generaciones,f'{ruta_carpeta}')

print('Mejor individuo:', mejor_individuo)
print('Distancia:', mejor_distancia)

ciudades = []

# Leer el archivo CSV
with open('/home/ale/META_H/TSP/matriz_distancias.csv', mode='r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:  
            ciudades = row

print('Ciudades correspondientes al mejor individuo:')
for idx in mejor_individuo:
    print(ciudades[idx])
guardar_aptitudes(generaciones, mejor_distancia,ruta_carpeta)



