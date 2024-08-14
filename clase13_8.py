def saludar():
    print("Hola, estamos saludando desde la función saludar() " \
            "del módulo clase13_8")
    
    











""" n = float(input("Introduce un número: "))
m = 4
print(n, "/", m, "=", n/m) """


""" print("Hola")



lista = []
if len(lista)>0:
    lista.pop()
 """





#TRY - EXCEPT

""" try:
    n = float(input("Introduce un número: "))
    m = 4
    print(n, "/", m, "=", n/m)
except:
    print("Algo salio mal") """
    
    
    
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print(n, "/", m, "=", n/m)
    except:
        print("Ocurrio un error, introduci un nro")
    else: 
        print("Todo sucedio correctamente")
        break

        
        
