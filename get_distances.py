from geopy.geocoders import Nominatim
from haversine import haversine
import csv
import time

# OBTENER CIUDADES EN LISTAS
with open('Ciudades.txt', 'r', encoding='utf-8') as file:
    ciudades = [line.strip() for line in file.readlines()]

print(ciudades)

# Función para obtener coordenadas de una ciudad
def obtener_coordenadas(ciudad):
    geolocalizador = Nominatim(user_agent="geoapi", timeout=10)  # Aumentamos el tiempo de espera a 10 segundos
    retries = 3  # Número de intentos de reintento
    for _ in range(retries):
        try:
            ubicacion = geolocalizador.geocode(ciudad)
            if ubicacion:
                return (ubicacion.latitude, ubicacion.longitude)
            else:
                print(f"No se pudo encontrar la ciudad: {ciudad}")
                return None
        except Exception as e:
            print(f"Error al obtener coordenadas para {ciudad}: {e}, reintentando...")
            time.sleep(5)  # Espera 5 segundos antes de reintentar
    print(f"No se pudo obtener la coordenada de {ciudad} después de varios intentos")
    return None

# Función para obtener la distancia entre dos ciudades
def obtener_distancias(ciudad1, ciudad2):
    coords1 = obtener_coordenadas(ciudad1)
    coords2 = obtener_coordenadas(ciudad2)
    if coords1 and coords2:
        distancia = haversine(coords1, coords2)
        return distancia
    else:
        print("No se pudo obtener la ubicación de alguna de las ciudades")
        return 0

# Crear la matriz de distancias
matriz_distancias = []

# Llenar la primera fila con los nombres de las ciudades
matriz_distancias.append([''] + ciudades)

# Llenar el resto de la matriz con las distancias entre cada par de ciudades
for i in range(len(ciudades)):
    fila = [ciudades[i]]  # Primer elemento es el nombre de la ciudad
    for j in range(len(ciudades)):
        if i == j:
            fila.append(0)  # La distancia de una ciudad consigo misma es 0
        else:
            distancia = obtener_distancias(ciudades[i], ciudades[j])
            fila.append(distancia)
    matriz_distancias.append(fila)

# Escribir la matriz de distancias en un archivo CSV
with open('matriz_distancias.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(matriz_distancias)

print("La matriz de distancias ha sido guardada en 'matriz_distancias.csv'")

