# Dado un tablero inicial (por ejemplo, una lista de listas de 8x8), donde la celda con "9" significa que hay una mina (que debe evitarse),
# y donde hay un "0" debe llenarse con el siguiente criterio: cada celda debe contener el número de nueves adyacentes que posee. La función
# que realiza esta tarea se llamará "agregar_numeros":

tablero = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 9, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 9, 0],
[0, 0, 9, 0, 0, 0, 9, 0],
[0, 0, 0, 0, 9, 0, 9, 0],
[0, 9, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 9, 0, 0, 0, 0],
[9, 0, 0, 0, 0, 9, 0, 0]
]

def agregar_numeros(tablero):
    desplazamientos = [(-1, -1), (-1, 0),(-1, 1),
    (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    tablero_completo = tablero.copy()
    largo = len(tablero)
    for fila in range(largo):
        for columna in range(largo):
            # Si encuentra mina, aumenta valor de vecinos.
            if tablero[fila][columna] == 9:         
                for desplz_fila, desplz_col in desplazamientos:
                    nueva_fila, nueva_columna = fila + desplz_fila, columna + desplz_col
                    if 0 <= nueva_fila < largo and\
                        0 <= nueva_columna < largo and\
                        tablero[nueva_fila][nueva_columna] != 9:
                        tablero_completo[nueva_fila][nueva_columna] += 1
    return tablero_completo

lista_final = colocar_numeros(tablero)
print(lista_final)
