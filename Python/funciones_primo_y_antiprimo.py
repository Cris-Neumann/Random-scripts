# La 1era funcion determina cuando un número es primo, para cualquier entero "a".
# La 2da funcion determina cuando un número es antiprimo (es decir, posee una cantidad de divisores mayor a cualquier entero menor a él) para cualquier entero "a".
# La 3era funcion muestra la cantidad de divisores comunes para cualquier para entero (a,b).
  
def es_primo(a):
    x=0
    suma=0
    for i in range(2,a):
        if a % i == 0:
            x=1
            suma=suma+x #suma es la cantidad de divisores acumulados, en el fondo
            break 
        else:
            x=0 
    if suma==0:
        respuesta=True
    elif suma!=0:
        respuesta=False
    return respuesta
    

def es_antiprimo(a):
    cant_divisores_enteros_previos = []
    for j in range(2,a+1):
        def es_divisor(j):
            x=0
            contador_de_divisores = 0
            for x in range(2,j+1):
                if ((j % x) == 0):  #and (j != x):
                    contador_de_divisores += 1
            #print("el numero ",j," tiene ",contador_de_divisores," divisores")
            cant_divisores_enteros_previos.append(contador_de_divisores)
        es_divisor(j) 
    mayor=1
    for k in range (0,a-3):
        if cant_divisores_enteros_previos[k] > 1:
            mayor = cant_divisores_enteros_previos[k]
    if cant_divisores_enteros_previos[a-2] > mayor:
        respuesta=True
    else:
        respuesta=False
    return respuesta

def divisores_comun(a,b):
    divisores_de_a = []
    divisores_de_b = []
    divisores_en_comun = []
    def es_divisor(j):
        x=0
        for x in range(2,j+1):
            if ((j % x) == 0):  #and (j != x):
                divisores_de_a.append(x)
    es_divisor(a)   
    def es_divisor(j):
        x=0
        for x in range(2,j+1):
            if ((j % x) == 0):  #and (j != x):
                divisores_de_b.append(x)
    es_divisor(b)   
    for i in divisores_de_a:
        for j in divisores_de_b:
            if i==j:
                divisores_en_comun.append(i)
    divisores_en_comun.append(1)    
    divisores_en_comun.sort()
    for w in divisores_en_comun:
        print(w)