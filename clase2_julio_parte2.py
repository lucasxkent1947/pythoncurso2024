# INICIO - INTERACCION 1 - INTERACCION 2 - INTERACCION 3 - FIN

# SENTENCIA DE CONTROL
# DOS TIPOS =  CONTROL CONDICIONAL Y CONTROL ITERATIVO

#LAS SENTENCIAS DE CONTROL DE FLUJO CONDICIONALES SE VANA  DEFINIR POR EL USO DE TRES PALABRAS CLAVES RESERVADAS:
#if, elif y else
# IF: SI
# ELIF: SINO, SI
# ELSE: SINO

#SENTENCIA IF:
# NOS PERMITE CONTROLAR EL FLUJO DE UN PROGRAMA Y DIVIDIR LA EJECUCIÓN DEL MISMO EN DIFERENTES CAMINOS.
# AL UTILIZAR ESTA PALABARA RESERVADA LE VAMOS A DECIR A PYTHON QUE QUEREMOS EJECUTAR UN BLOQUE DE CODIGO SOLO SI SE CUMPLE DETERMINADA CONDICION, ES DECIR, SI EL RESULTADO ES TRUE.


""" edad= int(input("Que edad tenés?"))
if edad >= 18:
    print("Sos adulto")

if False:
    print("IMPRIMIME LA CONDICION VERDADERA") """


a = 2
b = 10
""" if a == 2:
    print("a vale", a)
    if b == 10:
        print("y b vale:", b)
         """
""" if a == 2 and b == 10:
    print("a vale",a, "y b vale", b) """

#ELSE 

""" numero = 24
if numero >=36:
    print("El numero es mayor o igual a 36")
else:
    print("El numero es menor a 36") """
    
#ELIF sino, si

""" dato_entrada = input("ESCRIBI ENTRAR, SALUDO O SALIR: ").upper()
if dato_entrada == "ENTRAR":
    print("Bienvenido")
elif dato_entrada == "SALUDO":
    print("Hola, como estás?")
elif dato_entrada == "SALIR":
    print("Te estás yendo")
else:
    print("No reconozco la interacción") """
    

""" nota = int(input("Escribí tu nota:"))
if nota >= 9:
    print("Sobresaliente")
elif nota >=7:
    print("Muy bien")
elif nota >=6:
    print("Bien")
elif nota >=4:
    print("Regular")
else:
    print("Desaprobaste") """
    
    
""" nota = int(input("Escribí tu nota:"))
if nota >= 9:
    print("Sobresaliente")
if nota >=7 and nota <9:
    print("Muy bien")
if nota >=6 and nota<7:
    print("Bien")
if nota >=4 and nota <6:
    print("Regular")
else:
    print("Desaprobaste")
 """

