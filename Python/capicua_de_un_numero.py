# La 1era funcion determina cuando un número es capicúa (es decir, cuando es similar una palabra palíndroma), para cualquier entero "a".
# La 2da funcion calcula el capicúa para cualquier entero "a".
# La 3era funcion muestra el capicúa más alto dentro (incluye sus combinaciones de dígitos) de cualquier entero "a".
  
def es_capicua(a):
    a=list(str(a))
    lista_al_reves=a[::-1]
    if a == lista_al_reves:
        return True
    else:
        return False

def calcular_capicua(a):
    capicua=es_capicua(a)        
    if capicua==True:
        return int(a)
        import sys
        sys.exit()
    while not capicua==True:
        a=list(str(a))
        numero_al_reves=a[::-1]
        #convierto listas en str, y luego en int:
        numero_al_reves=int("".join(numero_al_reves))
        a=int("".join(a))
        a = a + numero_al_reves
        capicua=es_capicua(a)
    return int(a)

def encontrar_capicua(a):
    lista_de_capicuas=[]
    largo=len(list(str(a)))
    a=list(str(a))
    from itertools import combinations
    for x in range(1,largo):
        #Extraigo las combinaciones en lista "a", de largo variable "x":
        combinaciones = combinations(a, x)
        for i in list(combinaciones):
            extracto=int("".join(i))
            capicua=es_capicua(extracto)
            if capicua==True:
                lista_de_capicuas.append(extracto)
    maximo=max(lista_de_capicuas)    
    if int(maximo)<10:
        return 0
    else:
        return int(maximo)
