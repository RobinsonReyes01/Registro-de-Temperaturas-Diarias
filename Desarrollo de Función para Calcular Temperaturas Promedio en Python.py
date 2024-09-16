def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad a partir de los datos proporcionados.

    :param datos_temperaturas: Un diccionario donde las claves son nombres de ciudades
                               y los valores son listas de listas con temperaturas diarias por semana.
    :return: Un diccionario con las temperaturas promedio de cada ciudad.
    """
    promedios = {}

    for ciudad, temperaturas in datos_temperaturas.items():
        # Inicializamos variables para el cálculo
        total_temp = 0
        total_dias = 0

        # Iteramos sobre cada semana de temperaturas
        for semana in temperaturas:
            # Sumamos todas las temperaturas de la semana
            total_temp += sum(semana)
            # Contamos cuántos días hay en la semana
            total_dias += len(semana)

        # Calculamos el promedio dividiendo la suma total por el número de días
        promedio = total_temp / total_dias

        # Redondeamos a dos decimales y guardamos en el diccionario de promedios
        promedios[ciudad] = round(promedio, 2)

    return promedios


# Ejemplo de uso
datos = {
    "Ciudad A": [[20, 22, 23, 21, 25, 24, 22],
                 [21, 23, 24, 22, 26, 25, 23],
                 [22, 24, 25, 23, 27, 26, 24],
                 [23, 25, 26, 24, 28, 27, 25]],
    "Ciudad B": [[18, 20, 21, 19, 23, 22, 20],
                 [19, 21, 22, 20, 24, 23, 21],
                 [20, 22, 23, 21, 25, 24, 22],
                 [21, 23, 24, 22, 26, 25, 23]],
    "Ciudad C": [[25, 27, 28, 26, 30, 29, 27],
                 [26, 28, 29, 27, 31, 30, 28],
                 [27, 29, 30, 28, 32, 31, 29],
                 [28, 30, 31, 29, 33, 32, 30]]
}
# calcula con datos de ejemplo
resultados = calcular_temperatura_promedio(datos)
# Da los resultados
print(resultados)