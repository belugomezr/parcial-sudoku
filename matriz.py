
import random

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor:int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = []
        for _ in range(cantidad_columnas):
            fila.append(valor)
        matriz.append(fila)
    return matriz

matriz = inicializar_matriz(9,9,0)

def dividir_en_regiones(matriz):
    regiones = []
    for fila_inicio in range(0, 9, 3):
        for col_inicio in range(0, 9, 3):
            region = [fila[col_inicio:col_inicio+3] for fila in matriz[fila_inicio:fila_inicio+3]]
            regiones.append(region)
    return regiones

def cargar_numeros(matriz, cantidad):
    for _ in range(cantidad):
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        numero_aleatorio = random.randint(1, 9)

        # si el casillero ya está ocupado, buscamos otro
        while matriz[fila][columna] != 0:
            fila = random.randint(0, 8)
            col = random.randint(0, 8)

        matriz[fila][columna] = numero_aleatorio

    return matriz

carga_de_numeros = cargar_numeros(matriz, 45)
print(carga_de_numeros)
