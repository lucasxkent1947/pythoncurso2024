# SENTENCIAS ITERATIVAS 
#WHILE
#FOR

# EL flujo de ejecucion de una sentencia WHILE:
#1. Evalua la condicion devolviendo FALSE O TRUE
#2. Si la condicion es FALSE, se sale sentencia WHILE y continua la ejecución con la siguiente sentencia.
#3. Si la condición es TRUE, ejecuta cada una de las sentencia que hay en el bloque del codigo y regresa el paso 1.

""" numero = 10
while numero >0:
    print(numero)
    numero-= 1
print("Terminó el conteo")
 """

""" n = 0
while n <=5:
    n+=1
    print("N vale ", n) """
    
#while condicion:
#   intrucciones de while
#else 
#   intrucciones de while-else
#si no se terminó con break
#   intrucciones de while-else



""" chance = 1
while chance <= 3:
    txt = input("Escribe SI: ")
    if txt == "SI":
        print("Ok, lo conseguiste en el intento", chance)
        break
    chance +=1
else:
    print("Has agotado tus tres intentos")
     """
    
# BREAK - CONTINUE - PASS
#BREAK CIERRA EL BUCLE CON UNA CONDICION EXTERNA
""" n = 5
while n < 10:
    n-=1
    if n == 2:
        print("ahora n vale 2 y salimos del bucle")
        break
    print("n vale", n)
 """
#CONTINUE SIRVE PARA OMITIR UNA PARTE DEL BUCLE EN LA CUAL SE ACTIVA UNA CONDICION EXTERNA

""" m = 0
while m < 10:
    m+=1
    if m==2:
        print("Continuamos con la siguiente iteración")
        continue
    print("m vale" ,m) """


#PASS sirve para manejar la condicion sin que el bucle se vea afectado de ninguna manera.

""" l = 0
while l < 10:
    l+=1
    if l ==2:
        pass
    print("l vale", l)
     """
    
    

#FOR 

""" lista = [1,2,3,123,5]

for valor in lista:
    print("Soy un item de la lista y valgo ", valor)
     """
    
#FOR = PARA 
#valor es simplemente una variable creada del objeto que se está iterando.
#IN = en
#lista es la lista, tupla, etc.. que va a ser iterada.. 


""" lista_1 = [0,1,2,3,4,5,6,7,8,9,10]
for num in lista_1:
    print("Soy el valor de la lista_1 y valgo ", num)
    num *=5
    print("Soy un valor de la lista_1 y ahora valgo", num)
    
 """
""" indice = 0
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *=5
    indice += 1
    #tambien se puede con indice = numero
print(numeros)


texto = "Hola mundo, estoy usando for en python"
for letra in texto:
    print(letra)
    
texto2 = ""
for letra in texto:
    texto2= letra *2
print(texto2)
 """

