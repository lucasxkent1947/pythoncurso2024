#Clase Martes 18 de Junio

#_________________________________NUMEROS_______________________________________

## NUMEROS ENTEROS = INT o LONG
##LONG 4564654564544645L


## NUMERO FLOAT = NUMEROS CON DECIMALES
## EJ: 0.32
# -33.895

# COMPLEX
## 33.8j

# SUMA +
# RESTA -
# MULTIPLICACIÓN *
# POTENCIA **
# DIVISIÓN (cociente) /
# DIVISIÓN (parte entera) //
# PROMEDIO %

# PROCEDENCIA DE LOS OPERADORES:
#1- TERMINOS ENTRE PARENTESIS
#2- POTENCIACION Y RAICES
#3- MULTIPLICACION Y DIVISION
#4- SUMA Y RESTA

""" print(15+8)

print(30.5-5)

print(80*2) """


#_____________________ STRING = STR (CADENA DE TEXTO)__________________________________

#COMILLAS DOBLES"" 
#COMILLAS SIMPLES''


print("Hola Mundo")

print("Un string \t con tabulacion")

print("Otro string pero con \n salto de linea ")


#___________ VARIABLES_________________
# LAS VARIABLES EN PYTHON SON COMO ETIQUETAS QUE NOS PERMITEN HACER REFERENCIA A LOS DATOS.
#POR CADA DATO QUE APARECE EN UN PROGRAMA, PYTHON VA A CREAR UN OBJETO QUE LO CONTIENE.
# CADA OBJETO VA A TENER:
#1- UN IDENTIFICADOR UNICO (id)
#2- UN TIPO DE DATO (entero, decimal, string, etc)
#3- UN VALOR (el propio dato dentro)
# LAS VARIABLES EN PYTHON NO GUARDAN LOS DATOS.


# definir una variable: a=2

mi_variable = 1947

print(mi_variable)

######### EL NOMBRE DE UNA VARIABLE SIEMPRE DEBE EMPEZAR POR UNA LETRA O POR UN GUION BAJO(_) snake_case
#LOS NOMBRES EN LAS VARIABLES NO PUEDEN INCLUIR ESPACIOS EN BLANCO
#PYTHON RECONOCE LAS MAYUSCULAS Y MINUSCULAS

mi_fecha_de_nacimiento = "02 de junio"

print(mi_fecha_de_nacimiento)

#METODO DE SALIDA = PRINT()

#METODO DE ENTRADA = INPUT()

""" nombre = input("Hola! Escribí tu nombre:")

print(nombre) """

print(30+9)


# LA FUNCIÓN INPUT POR DEFECTO CONVIERTE LOS DATOS DE ENTRADA EN UN STRING (ES UNA CADENA). AUNQUE LE ESTEMOS ESCRIBIENDO UN NUMERO


a = 20
b = 30

resultado = a+b

print(resultado)

c = 100
d = 200

print(c+d)

# LOS DATOS DE ENTRADA SE PODRIAN CONVERTIR DE STR (STRING)

e = 30
""" f = input("Cual es tu edad?") """ # este es un ejemplo de un dato de entrada que lo toma como cadena de texto
""" f = int(input("Cual es tu edad")) """ # CONVERSION DE TIPO: De esta forma logramos que python convierta el STR de entrada en un NUMERO



""" print(e*f) """


cadena_de_texto = "Python SOS LO MEJOR DE MI VIDA TKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM YO"
anio_del_curso = "2024"

print(cadena_de_texto + anio_del_curso)

#A LAS SUMA DE LOS STRINGS LO VAMOS A LLAMAR CONCATENACIÓN

# LOS INDICES VIENEN: 0 (primer caracter), 1 (segundo caracter), etc..
# LOS INDICES INVERSOS: -1(ultimo caracter), -2 (penultimo), etc.. 
# P   Y  T  H  O  N
# 0   1  2  3  4  5 indices
# -6 -5 -4 -3 -2 -1 indice inverso
print(cadena_de_texto[-1])