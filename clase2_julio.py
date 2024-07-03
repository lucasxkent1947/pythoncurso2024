


#___OPERADORES 

# Operando [operador] Operando
#            - / * +  
# operadores aritmeticos (+, -,*, /) 
# expresiones aritmeticas: 2+2, 5-1, -1.9 * 100, 20/3
# expresiones algebraicas: radio * 3.14 (nota1 + nota2)/2

# Tipo Logico: BOOLEANO o binario
# Es el tipo de dato más basico de  la informacion racional y representa VERDADERO y FALSO

#NEGACION
# No Verdadero = Falso (FALSE)
# No falso= Verdadero (TRUE)

# OPERADORES RELACIONALES
#Los operadores relacionales son simbolos que se usan para comparar dos valores. Si el resultado de la comparacion es correcto, la expresión vaa ser considerada TRUE, de lo contrario será FALSE.

""" print( 1+1 ==3 ) """

#IGUALDAD 
#El operador de igualdad sirve para preguntarle al programa si ambos operandos son iguales.
#Nos va a devolfer TRUE si son iguales, y FALSE si son distintos
# ESTE OPERADOR SE ESCRIBE CON DOS SIGNOS IGUAL (==)

a = 3

print(a == 3)

#DESIGUALDAD o DISTINTO
#El operador DISTINTO sirve para preguntarle a nuestro programa si ambos operandos son distintos.
#Va a devolver TRUE si son distintos, y FALSE sin son iguales
#Este Operador se escribe con un signo de exclamación y un signo de igual (!=)

print( a != 3)

# MENOR QUE
#El operador MENOR QUE sirve para preguntarle a nuestro programa si el primer operando es menor que el segundo operando
#Nos va a devolver TRUE si el primero es menor al segundo y FALSE si el primero es mayor que el segundo.
#Este operador se escribe con un signo de menor (<)
# 7 < 3
print( 7<3)


# MENOR IGUAL QUE
#El operador MENOR IGUAL QUE sirve para preguntarle a nuestro programa si el primer operando es menor que el segundo operando O si ambos son iguales
#Nos va a devolver TRUE si el primero es menor o igual al segundo, y FALSE si el primero es mayor que el segundo.
#Este operador se escribe con un signo menor que y un igual (<=)
print( 7<=3)
print(10<=10)


#MAYOR QUE 
# El operador MAYOR QUE sirve para preguntarle a nuestro programa si el primer operando es mayor que el segundo operando.
#Nos va a devolver TRUE si el primero es mayor al segundo y FALSE si el primero es menor que el segundo. 
# Este operador se escribe con un signo demayor que (>)

print(7>6)
print(1>2)

# MAYOR  IGUAL QUE
#El operador MAYOR IGUAL QUE sirve para preguntarle a nuestro programa si el primer operando es mayor que el segundo operando O si ambos son iguales
#Nos va a devolver TRUE si el primero es mayor o igual al segundo, y FALSE si el primero es menor que el segundo.
#Este operador se escribe con un signo mayor que y un igual (>=)
print(7>=3)
print(10>=10) 



#Podemos hacer operaciones relacionales en strings inclusive.

print("Hola" =="Hola")

b = "Hola"

print(b[1] == "o") # Acá le estoy pidiendo al programa que me diga si el indice 1 de la variable b es igual a "o"



""" False == True -falsa
10 >= 2*4 - verdadera
33/3 == 11 -verdadera
True > False - verdadera
True*5 == 2.5*2 -verdadera  """

print(True*5 == 2.5*2)



#_______________ OPERADORES LOGICOS
#NOT 
#NOT es la negación, o tambien conocido como NO. Solo afecta a los tipos logicos TRUE Y FALSE y solo requiere un operando en una expresion.
print(not True == False)


#Conjunción y Disyunción
#Conjunción viene de conjunto, agrupa uniendo
#Disyunción viene de disyunto, agrupa separando.

#AND  es conocido como el Y
#Va a unir una o varias sentencias logicas.
#Verdadero Y Verdadero

print ( 2> 1 and 5 > 2) 
print( 5> 25 and 20<1)


#True AND True - True
#True AND False - False
#False AND False - False
#False and True - False

#OR es O en ingles.
#Es Disyunción (separa)
# Si le pregunto a python por dos afirmaciones y al menos una es TRUE, python me va a decir que la afirmación es TRUE

print(2>1 or 5>2)
print(5<20 or 20<1)

# True o True - True
# True o False - True 
# False o True - True
# False o False - False 




#Ejercicio Mental Expresiones
# not False - verdadero
# not 3 == 5 - verdadero
# 33 /3 == 11 and 5>2 - verdadero
#True or False - verdadero
# True*5 == 2.5*2 or 123>= 23 - verdadero
# 12> 7 and True < False - falso

#NORMAS DE PRECEDENCIA
#1. TERMINOS ENTRE PARENTESIS
#2. POTENCIACIÓN Y RAICES
#3. MULTIPLIACIÓN Y DIVISIÓN
#4. SUMA Y RESTA

d = 15
e = 12
print(d**e / 3 **e / e * d >= 15 and not (d%e **2) != 0)

numero = 15

a = 0
a +=1

print(a)

b = 50
b -=5
b -=5
b -=5
print(b)

c = 5
c *= 10
c *= 10
c *= 10
print(c)


#  Operador         Ejemplo     Equivalente
#  =                 a = 2         a = 2
#  +=                a += 2        a = a + 2
#  -=                a -= 2        a = a - 2
# *=                a *= 2        a = a * 2
# /=                a /= 2        a = a / 2
#  %=
# **= 



