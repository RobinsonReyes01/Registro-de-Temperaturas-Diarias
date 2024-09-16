import numpy as np

ciudades = ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
num_semanas = 4

temperaturas = np.random.randint(10, 36, size=(len(ciudades), len(dias_semana), num_semanas))

for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura para {ciudad}:")
    for semana in range(num_semanas):
        promedio = np.mean(temperaturas[ciudad_idx, :, semana])
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")

def obtener_promedio(ciudad, semana):
    return np.mean(temperaturas[ciudades.index(ciudad), :, semana])


for ciudad in ciudades:
    for semana in range(num_semanas):
        promedio = obtener_promedio(ciudad, semana)
        print(f"\nEl promedio de temperatura en {ciudad} para la semana {semana + 1} es: {promedio:.2f}°C")