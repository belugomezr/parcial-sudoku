
import random

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor:int) -> list: #Inicializo la matriz
    matriz = []
    for i in range(cantidad_filas):
        fila = []
        for _ in range(cantidad_columnas):
            fila.append(valor)
        matriz.append(fila) #Añade la fila completa a la matriz.
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

def validar_numero(matriz, fila, columna, numero): #validamos el numero 
    if numero == 0:
        return True  
    valor_anterior = matriz[fila][columna]
    matriz[fila][columna] = 0
    fila_ok = not chequear_fila(matriz, fila, numero)
    columna_ok = not chequear_columna(matriz, columna, numero)
    region_ok = not chequear_region(matriz, fila, columna, numero)

    matriz[fila][columna] = valor_anterior
    return fila_ok and columna_ok and region_ok #retorna el numero si es que pasa todos los chequeos

def encontrar_vacio(matriz): #busca la siguiente celda vacia para ingresar otro numero (donde)
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 0:
                return i, j
    return None

def generar_tablero_completo():
    matriz = [[0]*9 for _ in range(9)]
    resolver_sudoku_aleatorio(matriz)
    return matriz

def region_completa(matriz, fila, columna):
    fila_vertice = (fila//3)*3
    columna_vertice = (columna//3)*3
    for i in range(3):
        for j in range(3):
            if matriz[fila_vertice + i][columna_vertice + j] == 0:
                return False
    return True

def resolver_sudoku_aleatorio(matriz): #Llena el tablero para lograr encontrar una solucion valida 
    pos = encontrar_vacio(matriz) 
    if pos is None: #sino hay celdas vacias retorna True
        return True
    fila, col = pos
    numeros = list(range(1, 10))
    random.shuffle(numeros)
    for numero in numeros: #recorre los numeros aletarios
        if validar_numero(matriz, fila, col, numero): 
            matriz[fila][col] = numero
            if resolver_sudoku_aleatorio(matriz):
                return True
            matriz[fila][col] = 0
    return False #esto permite probar otras combinaciones

def resolver_sudoku_conteo(matriz, limite=2): #Verificamos que tenga al menos dos soluciones 
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
        if validar_numero(matriz, fila, col, num): #Intentamos cada número posible en la celda vacía, validando fila, columna y región
            matriz[fila][col] = num
            soluciones += resolver_sudoku_conteo(matriz, limite) 
            if soluciones >= limite:
                break

            matriz[fila][col] = 0

    return soluciones

def tablero_completo(matriz):
    for fila in matriz:
        if 0 in fila:
            return False
    return True

def generar_tablero_facil_por_region(numeros_por_region): #genera los numeros por region y dificultad
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

def crear_sudoku_con_pistas(tablero_completo, pistas_por_region=5):
    sudoku = [fila[:] for fila in tablero_completo] #hace una copia del tablero completo para no modificar el original

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

    return sudoku #Devuelve el Sudoku jugable con las pistas finales

def region_correcta(matriz, region_f, region_c):
    numeros = []
    for f in range(region_f*3, region_f*3+3):
        for c in range(region_c*3, region_c*3+3):
            num = matriz[f][c]
            if num == 0:
                return False   # incompleta
            numeros.append(num)
    return len(numeros) == 9 and len(set(numeros)) == 9  # sin repetidos

def actualizar_puntaje(puntaje, matriz, fila, columna, numero, celda_incorrecta): 
    if validar_numero(matriz, fila, columna, numero):
        puntaje += 1
        if tablero_completo(matriz):
            puntaje += 81
    else:
        if not celda_incorrecta:
            puntaje -= 1
    return puntaje

def actualizar_puntaje_regiones(matriz, regiones_completadas, puntaje):
    for rf in range(3):
        for rc in range(3):
            if not regiones_completadas[rf][rc]:  
                if region_correcta(matriz, rf, rc):
                    puntaje += 9
                    regiones_completadas[rf][rc] = True
    return puntaje