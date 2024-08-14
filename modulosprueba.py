""" import clase13_8

clase13_8.saludar() """
 

""" from clase13_8 import saludar
saludar()

from clase13_8 import *
saludar() """

""" from collections import Counter
b = [1,4,3,5,1,2,3,9,2,7]
print(Counter(b))
print(Counter("palabritas")) """

""" from collections import defaultdict
d = defaultdict(str)  # tipo cadena por defecto
print(d["cosa"])
print(d) """


""" from collections import OrderedDict
m = OrderedDict()
m["uno"] = "one"
m["dos"] = "two"
m["tres"] = "three"
print(m) """


""" from datetime import datetime

dt = datetime.now()    # Fecha y hora actual

print(dt)
print(dt.year)         # año
print(dt.month)        # mes
print(dt.day)          # día

print(dt.hour)         # hora
print(dt.minute)       # minutos
print(dt.second)       # segundos
print(dt.microsecond)  # microsegundos

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}".format(dt.day, dt.month, dt.year)) """



""" import math

print(math.floor(4.99))  # Redondeo para abajo 
print(math.ceil(2.01))   # Redondeo para arriba

numeros = [0.9999999, 5, 7, 1]
print(math.fsum(numeros))

print(math.pow(2, 3))  # Potencia con flotante 
print(math.sqrt(9))    # Raíz cuadrada """



import random

# Flotante aleatorio >= 0 y < 1.0
print(random.random())      

# Flotante aleatorio >= 1 y <10.0       
print(random.uniform(1,10))

# Entero aleatorio de 0 a 19, 20 excluído
print(random.randrange(20))

# Entero aleatorio de 0 a 1000
print(random.randrange(0,1001))

# Entero aleatorio de 0 a 1000 cada 2 números, múltiples de 2
print(random.randrange(0,1001,2))

# Entero aleatorio de 0 a 1000 cada 5 números, múltiples de 5
print(random.randrange(0,1001,5))

# Letra aleatoria
print(random.choice("Dale Morón"))

# Elemento aleatorio
print(random.choice([1,2,3,4,5]))

# Dos elementos aleatorios
print(random.sample([1,2,3,4,5], 2))

# Mezclar una lista, queda guardado
lista = [1,2,3,4,5]
random.shuffle(lista)
print(lista)