
import random


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

def es_valido(matriz, fila, columna, numero):
    if chequear_fila(matriz, fila, numero):
        return False
    if chequear_columna(matriz, columna, numero):
        return False
    if chequear_region(matriz, fila, columna, numero):
        return False
    return True


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


def encontrar_vacio(matriz):
    for f in range(9):
        for c in range(9):
            if matriz[f][c] == 0:
                return f, c
    return None


def resolver_sudoku(matriz):
    vacio = encontrar_vacio(matriz)
    if vacio is None:
        return True  # Sudoku completo

    fila, columna = vacio

    for num in range(1, 10):
        if not chequear_fila(matriz, fila, num) and \
           not chequear_columna(matriz, columna, num) and \
           not chequear_region(matriz, fila, columna, num):

            matriz[fila][columna] = num

            if resolver_sudoku(matriz):
                return True

            matriz[fila][columna] = 0  # backtrack

    return False

def generar_tablero_completo():
    matriz = [[0]*9 for _ in range(9)]

    def resolver_aleatorio(m):
        for f in range(9):
            for c in range(9):
                if m[f][c] == 0:
                    numeros = list(range(1, 10))
                    random.shuffle(numeros)  # ← ¡clave para evitar la escalera!

                    for n in numeros:
                        if not chequear_fila(m, f, n) and \
                           not chequear_columna(m, c, n) and \
                           not chequear_region(m, f, c, n):

                            m[f][c] = n

                            if resolver_aleatorio(m):
                                return True

                            m[f][c] = 0
                    return False
        return True

    resolver_aleatorio(matriz)
    return matriz


def crear_sudoku_con_pistas(tablero_completo, pistas_por_region=5):
    sudoku = [fila[:] for fila in tablero_completo]  # copiar matriz

    for reg_f in range(3):
        for reg_c in range(3):
            # generar posiciones dentro de la región 3x3
            posiciones = [(reg_f*3 + i, reg_c*3 + j) for i in range(3) for j in range(3)]
            random.shuffle(posiciones)

            # dejar solo 5 números, vaciar el resto
            for f, c in posiciones[pistas_por_region:]:
                sudoku[f][c] = 0

    return sudoku

def casilla_editable(tablero_inicial, fila, columna):
    return tablero_inicial[fila][columna] == 0