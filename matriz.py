
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


def chequear_fila(matriz:list, fila:int, numero:int): #matriz, fila y numero que quiero buscar 
    retorno = False
    for i in range(9): #recorro las filas de mi matriz 
        if matriz[fila][i] == numero: #comparo el valor con el numero que estoy buscando
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
    max_numeros_por_region = (int) (cantidad / 9)

    for fila_region in range(3): #recorre regiones (0,1,2)
        for columna_region in range(3):
            for _ in range(max_numeros_por_region): 
                numero_repetido = True
                numero_aleatorio = 0
                
                fila = random.randint(0, 2) + (fila_region * 3) 
                columna = random.randint(0, 2) + (columna_region * 3) 
                # si el casillero ya está ocupado, buscamos otro
                while matriz[fila][columna] != 0:
                    fila = random.randint(0, 2) + (fila_region * 3)
                    columna = random.randint(0, 2) + (columna_region * 3)

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

