#                            Conjuntos  / SET
""" conjunto = {1,2,3,4,5}
otro_conjunto = {"hola", "como", "estas", "?"}
conjunto_vacio = set()
 """
#Son heterogeneos
""" variable1 = "esto es una variable"
datos = {1,-5,123.57, "una cadena", "otro string", variable1}
print(datos) """

#Puede incluir numeros, variables, strings, o tuplas.
#Pero NO puede incluir objetos mutables como listas, diccionarios e incluso otros conjuntos.


""" lista = ({1,2,3,4,5})
print(lista)
print(set([1,1,2,2,2,3,3,4,4])) """


#FUNCIONES INTEGRADAS EN SET/CONJUNTOS
#ADD
""" numeros = {1,2,3,4}
numeros.add(5)
print(numeros) """

#UPDATE
numeros = {1,2,3,4}
numeros.update([5,6,4,7,8])
print(numeros)

#LEN 
print(len(numeros))

#DISCARD
numeros.discard(2)
print(numeros)

#REMOVE 
#REMOVE y DISCARD funcionan de igual manera, a diferencia que en DISCARD si el elemento pasado como argumento no existe, lo ignora. En cambio con REMOVE nos devolverá un error.


#IN
print(3 in numeros)

#CLEAR 
""" numeros.clear() """

#POP
""" numeros1 = {1,2,3,4,5,6}
while numeros1:
    print("Se esta borrando: ", numeros1.pop()) """
    
#                                DICCIONARIO / DICT

colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}

print(colores["amarillo"])

colores["amarillo"] = "white"
print(colores)

edades = {"Juan": 26, "Esteban": 35, "Maria": 29}
edades["Juan"] +=5
edades["Maria"] *=2
print(edades)


#ADD 
numeros3 = {"uno": 1, "dos" : 2, "tres": 3, "cuatro": 4}
numeros3["cinco"] = 5
print(numeros3)

#UPDATE 
numeros3.update({"seis":6})
print(numeros3)


#LEN 
print(len(numeros3))

#DEL 
del numeros3["dos"]
print(numeros3)

#IN 
print("tres" in numeros3 )

#CLEAR 
""" numeros3.clear() """

#POP
print(numeros3.pop("uno"))



