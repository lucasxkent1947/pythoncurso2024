#Longitud de String
# Funcion LEN 

""" esto_es_un_string = "Hola soy un string"

print(len(esto_es_un_string))

string1= "    "
print(len(string1))
 """

#Rebanar un string 
# Funcion SLICING [inicio:fin:paso]
#Inicio va a ser el indice del primer caracter de la cadena que queremos rebanar.
#Fin va a ser el indice del ultimo caracter no incluido de la cadena que queremos rebanar.
#Paso: indica cada cuantos caracteres seleccionaremos entre las posiciones de inicio y fin

""" saludo = "Hola, como estan?"
print(len(saludo))
saludo[0:3:1]
print(saludo[0:3:1])

print(saludo[0:17:2])


palabra = "Pithon"
print(palabra)

print(palabra[1])

palabra = palabra[0:1] +"y"+ palabra[2:]

print(palabra)
 """
### LISTA Y TUPLAS

""" mi_lista = [-11,20,3,41]
print(mi_lista)

otra_lista = ["Hola", "Como", "Estas", "?"]

variable_1 = "Una variable"

listita = [1, -10, 132.5, "Un string", "Otro string", variable_1]

print(listita)


print(listita[0])
print(listita[-1])

print(listita[-2:])

print(listita + [otra_lista, "ALGO RANDOM"]) """

""" numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros+[11,12,13,14,15,16])

numeros = [99999,2,4,5,10,15,20]
numeros[3] = 8
print(numeros)


letras = ["a", "b", "c", "d", "e", "f"]
letras[:3] = ["A", "B", "C"]
print(letras)

letras = ["a", "b", "c", "d", "e", "f"]
letras[:3] = []
print(letras)

equipos = ["Moron", "River", "Boca", "Independiente"]
print(equipos)
equipos = []
print(equipos) """


#FUNCION APPEND
#Nos permite agregar un nuevo item al final de una lista - Se escribe mi_lista.append(item_a_agregar)
numeros = [1,2,3,4,5,6]
numeros.append(7)
print(numeros)

#Tambien podemos utilizar la funcion LEN acá - LEN se escribe len(la_lista_a_consultar_su_longitud)
print(len(numeros))

""" equipos = ["Moron", "River", "Boca", "Independiente"]
print(equipos)
print(len(equipos)) """

#FUNCION POP
#La funcion todo lo contrario a Append, porque va a eliminar el ultimo item de una lista. - pop.() 

""" equipos = ["Moron", "River", "Boca", "Independiente"]
equipos.pop()
print(equipos) """
#Si ingreso dentro del parentesis una posicion segun indice, POP elimina el indice correspondiente.
equipos = [1, 2, 3, 4]
equipos.pop(2)
print(equipos)

# FUNCION COUNT
# La funcion COUNT cuenta el numero de veces que nuestro item se repite en una lista. - SE ESCRIBE la_lista_a_contar.count(el_item_que_queremos_que_cuente)
numeros_varios = [1,2,3,5,9,12,55,20,20,20,3,5,59]
#En este caso el item 20, se repite 3 veces
print(numeros_varios.count(20))

#INDEX
#Busca el item y nos devuelve en que indice está - SE ESCRIBE la_lista.index(lo_que_queremos_buscar)

numeros_varios = [1,2,3,5,9,12,55,20,20,20,3,5,59]
print(numeros_varios.index(59))


##_______________ TUPLAS
#Las tuplas son similares a las listas, la GRAN diferencia es que las tuplas son INMUTABLES.
# Se declaran con parentesis - mi_tupla(1,2,3,4)

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

otra_tupla = (1,5,-100, "Cadena", "Otra cadena/string", mi_tupla)

print(otra_tupla)

print(otra_tupla[0])

print(otra_tupla[2:])



print(len(otra_tupla))

print(otra_tupla.index(5))

print(otra_tupla.count(1))
