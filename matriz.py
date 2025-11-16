
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


def chequear_fila(matriz:list, fila:int, numero:int):
    retorno = False
    for i in range(9):
        if matriz[fila][i] == numero:
            retorno = True
    return retorno

def chequear_columna(matriz:list, columna:int, numero:int):
    retorno = False
    for i in range(9):
        if matriz[i][columna] == numero:
            retorno = True
    return retorno

def chequear_region(matriz:list, fila:int, columna:int, numero:int):
    retorno = False
    fila_vertice = (int) (fila/3) * 3
    columna_vertice = (int) (columna/3) * 3

    for i in range(3):
        for j in range(3):
            if matriz[i + fila_vertice][j + columna_vertice] == numero:
                retorno = True

    return retorno


def cargar_numeros(matriz:list, cantidad:int):
    for _ in range(cantidad):
        numero_repetido = True
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        numero_aleatorio = 0

        # si el casillero ya está ocupado, buscamos otro
        while matriz[fila][columna] != 0:
            fila = random.randint(0, 8)
            columna = random.randint(0, 8)

        while(numero_repetido == True):
            numero_aleatorio = random.randint(1, 9)
            numero_repetido = False

            if chequear_fila(matriz, fila, numero_aleatorio) == True:
                numero_repetido = True
            elif chequear_columna(matriz, columna, numero_aleatorio ) == True:
                numero_repetido = True
            elif chequear_region(matriz, fila, columna, numero_aleatorio) == True:
                numero_repetido = True
        
        if numero_repetido == False:
            matriz[fila][columna] = numero_aleatorio

    return matriz

numeros_cargados = cargar_numeros(matriz, 45)
print(numeros_cargados)
