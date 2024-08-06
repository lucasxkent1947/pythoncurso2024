#SINTAXIS PARA DEFINIR UNA FUNCION
""" def NOMBRE(PARAMETROS):
    SENTENCIAS
    RETURN [EXPRESION] """

#NOMBRE: ES EL NOMBRE DE LA FUNCION
#PARAMETROS: en las funciones cuando recibe argumentos se lo denomina parametros.
#SENTENCIA: ES EL BLOQUE DE CODIGO
#RETURN: ES UNA SENTENCIA DE PYTHON QUE LE INDICA A LA FUNCION QUE DEVOLVER CUANDO LA LLAMEMOS
#EXPRESION: ES LO QUE DEVUELVE LA SENTENCIA RETURN

""" def saludar():
    print("Hola, los estoy saludando")
#PARA LLAMARLA ESCRIBIMOS EL NOMBRE DE LA FUNCION
saludar() """

""" def test():
    variable_test = 10
    print(variable_test)
test()
 """

""" def test3():
    return[1,2,3,4,5]

print(test3())
print(test3()[1])
print(test3()[1:4])

lista = test3()
print(lista[-1])

def test4():
    return print("Hola", 30, [1,2,3,4,5,6,7,8])
test4() """

""" def resta(numero1, numero2):
    return numero1 - numero2

r = resta (numero1 = 7, numero2 = 9)
print(r) """

""" def duplicar_valor(numero):
    for i,n in enumerate(numero):
        numero[i] *=2

lista2= [10,50,100]
duplicar_valor(lista2)


numero = 10
duplicar_valor(numero)
print(numero) """


 
""" def duplicar_valor(numero):
    for i, n in enumerate(numero):
        numero[i] *= 2

lista2 = [10, 50, 100]
duplicar_valor(lista2)
print(lista2)

 """
 
""" def duplicar_valor1(numero):
    numero*=2

numero = 10
duplicar_valor1(numero)
print(numero) """


""" def cuenta (numero):
    numero -=1
    if numero>0:
        print(numero)
        cuenta(numero)
    else:
        print("Termino")
cuenta(10) """

""" def calculo_factorial(numero):
    print("valor inicial", numero)
    if numero > 1:
        numero = numero * calculo_factorial(numero -1)
    print("Valor final", numero)
    return numero
print(calculo_factorial(5)) """


print(int(2.5))
print(int("307"))

#Acá si le verificamos el tipo nos muestra que el entero se transformo a string
print(type(str(50)))

print(float(25))
print(float("2.5"))



print(round(2.6))