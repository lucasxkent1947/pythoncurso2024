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


edad= int(input("Que edad tenés?"))
if edad >= 18:
    print("Sos adulto")

if False:
    print("IMPRIMIME LA CONDICION VERDADERA")
