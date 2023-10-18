'''Tenemos una lista y queremos recorrer dicha lista, de normal se haria con un for pero lo podemos hacer tambien
con un while de la siguiente forma.'''

#Tenemos una lista de numeros DEFINIDA
numeros = [10,20,30,40,50,60,70,80,90,100]
#Con un while podemos hacer que se recorra toda la lista de la siguiente forma

'''Primero definimos una variable indicie la cual dentro del while se ira incrementando. 
Esto nos sirve ya que el indice que se ira incrementando sera el indice de la lista pero para que se incremente 
y recorra toda la lista tenemos que incrementarlo de forma manual.'''
indice = 0 

'''Ahora empezamos el bucle while, lo que hacemos es que mientras que indice sea menor a el tamaño de la lista
"numeros" imprimiremos el numero que se encuentre en ese indice, y luego imprimiremos ese indice, es decir, 
imprimimos el numero 10 con indice 0. Luego al final del todo hacemos que se incremente el numero del indice 
para que mientras que hayan indices (0,1,2,3...) se vaya incrementando solo y saque los numeros en su indice 
correspondiente'''
while indice < len(numeros):
    print(numeros[indice], "con indice", indice)
    indice +=1

'''--------------------------------------------------------------------------------------------------------------'''

#TENEMOS OTRA ALTERNATIVA MUCHO MAS VIABLE QUE ES HACERLO CON UN BUCLE "FOR"

'''Primero seteamos la lista que queramos imprimir, es decir que sabemos el tamaño de la lista (aunque no
necesariamente tengas que saberte la longitud de ella, es decir puede ser 100 o 1000000000. Mientras sea una 
lista definida que no cambiara en el momento de imprimir los valores podemos imprimirla sin problemas.) 
Asi pues tambien declaramos una variable indice (solo en caso de que queramos el valor del indicie en el
que se esta moviendo el for)'''
indice = 0
numeros = [10,20,30,40,50,60,70,80,90,100]
#Esto imprime el valor junto a su indice de posicion
#El enumerate primero de te devuelve la posicion y luego el valor
for indice, num in enumerate(numeros):
    print("valor", num, " --> indice:", indice)
   

"""Ahora con un bucle for con indice "i" (este indice puede tener cualquier otro nombre, no necesariamente tiene
que ser "i", yo le llamo asi por que en Java el for por defecto tiene una variable "i" de iterance),
le indicamos con un "in" el nombre de la lista que queramos que imprima, en mi caso será la de "numeros"
Esta es una forma de hacerlo, pero si queremos que nos de el indice tenemos que hacer una variable indice.
Asi podemos tambien podemos multiplicar los numeros de la lista

Imprime nada mas el valor de la lista 

for i in numeros: 
    print(i)"""


'''-------------------------------------------------------------------------------------------------------'''

'''Podemos sacar el tambien las letras por separado. O podemos contar cuantas letras (espacios incluidos) tiene una
oracion'''

texto = "Aprendiendo a Programar en Python"
contador = 0
#Para contar las letras en el texto necesitamos el metodo enumerate(texto que queramos saber su longitud)
for contador, letra in enumerate(texto):
    print (letra, "--> indice:",contador)
    
    
#Con esto mismo podemos saber en que posicion se encuentra una determinada letra, por ejemplo una a (con if's)

texto = "Aprendiendo a Programar en Python"
indice = 0
contador = 0
for indice, letra in enumerate(texto):
    #Esto dice que si en el texto hay alguna letra "A" o "a" te imprima su posicion y cual de las dos es
    if letra == "A" or letra == "a":
        print (letra, "esta en la posicion:", indice)
        #El contador es para contar las "a y A" que hayan en el texto
        contador += 1 #contador = contador + 1
        print("El numero de 'a' totales son:", contador)
        
'''------------------------------------------------------------------------------------------------------------'''
#PODEMOS MEZCLAR BUCLES Y CONDICIONALES PARA HACER COSITAS

'''Quiero saber cuales son los paises que hablan ESpañol, INgles o alguno otro y que queden identificados
y contar los paises de habla española, inglesa y los nos registrados'''


idiomas = ["ES_ESpaña", "EN_USA", "IT_Italia", "EN_United Kingdom", "ES_Venezuela", "RU_Rusia"]
#Variables para contar los paises de habla inglesa, española y los no registrados
contES = 0
contEN = 0
contUNK = 0

#bucle for para recorrer la lista
for codigo in idiomas:
   # print(codigo[3:])
   #Slicing para sacar el codigo de pais para el que necesitamos
    codigo_pais = codigo[:2]
    #Condicionales para los determinados codigos postales
    if (codigo_pais == "ES"):
        print(codigo[3:], "Este pais habla español")
        #Cont para cuando detecte un pais de habla española sume 1 al contador
        contES += 1
    elif (codigo_pais == "EN"):
        print (codigo[3:], "este pais habla ingles")
         #Cont para cuando detecte un pais de habla inglesa sume 1 al contador
        contEN +=1
    else:
        print (codigo[3:], "Este pais no tiene el idioma de origen registrado")
        #Cont para cuando detecte un pais de habla desconocida sume 1 al contador
        contUNK +=1

#fuera del for quiero escribir 3 mensajes, que son el recuento de todos los paises con su respectivo idioma de habla
print("*"*60)
print("El numero de paises que hablan Español son:", contES)
print("El numero de paises que hablan Ingles son:", contEN)
print("El numero de paises que hablan idiomas no registrados son:", contUNK)

'''Esto se puede hacer de otra forma, la cual es mas practica, lo cual consiste en guardar en sublistas los 
resultados de los paises, es decir, lo siguiente. Ademas con esto puedes guardar los paises y por si necesitas
el numero de los paises en la lista es mas facil sacarlos de ahi que contarlos uno a uno como se mostro anteriormente'''

'''Si nos dan el Strign del codigo del pais en minisculas pero nosotros lo buscamos en mayusculas, para asegurarnos
que aparezca nos aseguramos si le metemos a la variable "codigo_pais" la funcion .upper'''
paisesES = []
paisesEN = []
paisesUNK = []

for codigo in idiomas:
    codigo_pais = codigo[:2]
    if (codigo_pais == "ES"):
        paisesES.append(codigo[3:])
    elif (codigo_pais == "EN"):
        paisesEN.append(codigo[3:])
    else:
        paisesUNK.append(codigo[3:])
    
print("*"*60)
print("El numero de paises que hablan Español son:", len(paisesES))
print("El numero de paises que hablan Ingles son:", len(paisesEN))
print("El numero de paises que hablan idiomas no registrados son:", len(paisesUNK))
    