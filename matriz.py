
import random

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor:int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = []
        for _ in range(cantidad_columnas):
            fila.append(valor)
        matriz.append(fila)
    return matriz

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

def validar_numero(matriz, fila, columna, numero):
    if numero == 0:
        return True   # una celda vacía NO es un error
    valor_anterior = matriz[fila][columna]
    matriz[fila][columna] = 0

    fila_ok = not chequear_fila(matriz, fila, numero)
    columna_ok = not chequear_columna(matriz, columna, numero)
    region_ok = not chequear_region(matriz, fila, columna, numero)

    matriz[fila][columna] = valor_anterior
    return fila_ok and columna_ok and region_ok

def encontrar_vacio(matriz):
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 0:
                return i, j
    return None

def resolver_sudoku_aleatorio(matriz):
    pos = encontrar_vacio(matriz)
    if pos is None:
        return True
    fila, col = pos
    numeros = list(range(1, 10))
    random.shuffle(numeros)
    for numero in numeros:
        if validar_numero(matriz, fila, col, numero):
            matriz[fila][col] = numero
            if resolver_sudoku_aleatorio(matriz):
                return True
            matriz[fila][col] = 0
    return False

def generar_tablero_completo():
    matriz = [[0]*9 for _ in range(9)]
    resolver_sudoku_aleatorio(matriz)
    return matriz

def generar_tablero_facil_por_region(numeros_por_region):
    matriz = inicializar_matriz(9, 9, 0)

    for region_fila in range(3):
        for region_col in range(3):
            intentos = 0
            puestos = 0
            while puestos < numeros_por_region:
                if intentos > 100:  # Si no se logra, resetear la región y reintentar
                    for i in range(3):
                        for j in range(3):
                            matriz[region_fila*3 + i][region_col*3 + j] = 0
                    puestos = 0
                    intentos = 0
                numero = random.randint(1,9)
                fila = random.randint(0,2) + region_fila*3
                col = random.randint(0,2) + region_col*3
                if matriz[fila][col] == 0 and validar_numero(matriz, fila, col, numero):
                    matriz[fila][col] = numero
                    puestos += 1
                else:
                    intentos += 1
    return matriz

def region_completa(matriz, fila, columna):
    fila_vertice = (fila//3)*3
    columna_vertice = (columna//3)*3
    for i in range(3):
        for j in range(3):
            if matriz[fila_vertice + i][columna_vertice + j] == 0:
                return False
    return True

def tablero_completo(matriz):
    for fila in matriz:
        if 0 in fila:
            return False
    return True

def actualizar_puntaje(puntaje, matriz, fila, columna, numero, celda_incorrecta):
    if validar_numero(matriz, fila, columna, numero):
        puntaje += 1
        if tablero_completo(matriz):
            puntaje += 81
    else:
        if not celda_incorrecta:
            puntaje -= 1
    return puntaje


# def generar_tablero_completo():
#     matriz = [[0] * 9 for _ in range(9)]

#     def resolver(m):
#         pos = encontrar_vacio(m)
#         if pos is None:
#             return True

#         f, c = pos
#         numeros = list(range(1, 10))
#         random.shuffle(numeros)

#         for numero in numeros:
#             if validar_numero(m, f, c, numero):
#                 m[f][c] = numero
#                 if resolver(m):
#                     return True
#                 m[f][c] = 0

#         return False

#     resolver(matriz)
#     return matriz

# def cargar_numeros(matriz, cantidad):
# #     intentos_max = 300  
#     intentos = 0

#     while cantidad > 0 and intentos < intentos_max:
#         fila = random.randint(0, 8)
#         columna = random.randint(0, 8)

#         # Si ya tiene número, salteamos
#         if matriz[fila][columna] != 0:
#             intentos += 1
#             continue

#         numero = random.randint(1, 9)

#         if validar_numero(matriz, fila, columna, numero):
#             matriz[fila][columna] = numero
#             cantidad -= 1   # cargamos un número válido
#         else:
#             intentos += 1   # no se pudo, sumamos intento

# def cargar_numeros(matriz:list, cantidad:int): 
#     max_numeros_por_region = cantidad // 9

#     for fila_region in range(3):
#         for columna_region in range(3):
            
#             for _ in range(max_numeros_por_region):
#                 numero_repetido = True
#                 numero_aleatorio = 0

#                 # Elegir celda dentro de la región
#                 fila = random.randint(0, 2) + fila_region * 3
#                 columna = random.randint(0, 2) + columna_region * 3

#                 # Si está ocupada, buscar otra
#                 while matriz[fila][columna] != 0:
#                     fila = random.randint(0, 2) + fila_region * 3
#                     columna = random.randint(0, 2) + columna_region * 3

#                 # Buscar número válido
#                 while numero_repetido:
#                     numero_aleatorio = random.randint(1, 9)
#                     numero_repetido = False

#                     if chequear_fila(matriz, fila, numero_aleatorio):
#                         numero_repetido = True
#                     elif chequear_columna(matriz, columna, numero_aleatorio):
#                         numero_repetido = True
#                     elif chequear_region(matriz, fila, columna, numero_aleatorio):
#                         numero_repetido = True

#                 # Colocar número
#                 matriz[fila][columna] = numero_aleatorio

#     return matriz



# def resolver_sudoku(matriz):
#     vacio = encontrar_vacio(matriz)
#     if vacio is None:
#         return True  # Sudoku completo

#     fila, columna = vacio

#     for num in range(1, 10):
#         if not chequear_fila(matriz, fila, num) and \
#            not chequear_columna(matriz, columna, num) and \
#            not chequear_region(matriz, fila, columna, num):

#             matriz[fila][columna] = num

#             if resolver_sudoku(matriz):
#                 return True

#             matriz[fila][columna] = 0  # backtrack

#     return False

# def generar_tablero_completo():
#     matriz = [[0]*9 for _ in range(9)]

#     def resolver_aleatorio(m):
#         for f in range(9):
#             for c in range(9):
#                 if m[f][c] == 0:
#                     numeros = list(range(1, 10))
#                     random.shuffle(numeros)  # ← ¡clave para evitar la escalera!

#                     for n in numeros:
#                         if not chequear_fila(m, f, n) and \
#                            not chequear_columna(m, c, n) and \
#                            not chequear_region(m, f, c, n):

#                             m[f][c] = n

#                             if resolver_aleatorio(m):
#                                 return True

#                             m[f][c] = 0
#                     return False
#         return True

#     resolver_aleatorio(matriz)
#     return matriz


def crear_sudoku_con_pistas(tablero_completo, pistas_por_region=5):
    sudoku = [fila[:] for fila in tablero_completo]

    # posiciones del tablero mezcladas
    posiciones = [(fila, col) for fila in range(9) for col in range(9)]
    random.shuffle(posiciones)

    for fila, col in posiciones:
        if sudoku[fila][col] == 0:
            continue

        valor_original = sudoku[fila][col]
        sudoku[fila][col] = 0

        copia = [fila[:] for fila in sudoku]
        soluciones = resolver_sudoku_conteo(copia)

        # si el sudoku ahora no tiene solución única → revertimos
        if soluciones != 1:
            sudoku[fila][col] = valor_original

        # limitar cantidad mínima de pistas
        pistas_totales = sum(1 for v in sum(sudoku, []) if v != 0)
        if pistas_totales <= pistas_por_region * 9:
            break

    return sudoku


def resolver_sudoku_conteo(matriz, limite=2):
    """
    Cuenta cuántas soluciones tiene el sudoku.
    Se detiene si encuentra más de 'limite'.
    """
    vacio = encontrar_vacio(matriz)
    if not vacio:
        return 1  # encontró una solución

    fila, col = vacio
    soluciones = 0

    for num in range(1, 10):
        if validar_numero(matriz, fila, col, num):
            matriz[fila][col] = num
            soluciones += resolver_sudoku_conteo(matriz, limite)

            if soluciones >= limite:
                break

            matriz[fila][col] = 0

    return soluciones



def region_correcta(matriz, region_f, region_c):
    numeros = []
    for f in range(region_f*3, region_f*3+3):
        for c in range(region_c*3, region_c*3+3):
            num = matriz[f][c]
            if num == 0:
                return False   # incompleta
            numeros.append(num)
    return len(numeros) == 9 and len(set(numeros)) == 9  # sin repetidos


def actualizar_puntaje_regiones(matriz, regiones_completadas, puntaje):
    for rf in range(3):
        for rc in range(3):
            if not regiones_completadas[rf][rc]:  # aun no sumó
                if region_correcta(matriz, rf, rc):
                    puntaje += 9
                    regiones_completadas[rf][rc] = True
    return puntaje