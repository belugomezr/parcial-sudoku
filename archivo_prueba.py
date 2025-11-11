def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, minimo: int, maximo: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [random.randint(minimo, maximo)
            for _ in range(cantidad_columnas)]
        matriz.append(fila)
    return matriz

matriz = inicializar_matriz(9, 9, 1, 9)

def mostrar_matriz(matriz:list): 
    for indice in range(len(matriz)):
        for j in range(len(matriz[indice])):
                print(matriz[indice][j], end = " ") 
        print(" ")

mostrar_matriz(matriz)

def dividir_en_regiones(matriz):
    regiones = []
    for fila_inicio in range(0, 9, 3):          # 0, 3, 6
        for col_inicio in range(0, 9, 3):       # 0, 3, 6
            region = [fila[col_inicio:col_inicio+3] for fila in matriz[fila_inicio:fila_inicio+3]]
            regiones.append(region)
    return regiones

regiones = dividir_en_regiones(matriz)
print(regiones)