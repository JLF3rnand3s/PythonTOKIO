'''Tenemos las principales diferencias aqui'''
tupla =("coleccion ordenada e inmutable, admite miembros duplicados")
lista =["coleccion ordenada y modificable, admite miembros duplicados"]
unSet ={"coliccion desordenada y no indexada. No hay miembros duplicados"}
diccionario ={"coleccion desordenada, modificable e indexada. No hay miembros duplicados"}

'''Para insertar datos en la posicion final de una lista se utiliza el append(). Para las tuplas u otras
colecciones se utiliza el .add() (Aunque tambien existe el metodo insert en las listas para definir que 
dato y en que posicion los quieres meter, es decir por ejemplo --> nombreLista.add(posicion, valor))

Para poder eliminar elementos de un "Set" tenemos un metodo llamado .discard("aqui metemos el nombre del elemento
a eliminar"), o tambien el .pop("esto borra un elemento al azar").
'''

#La estructura de los diccionarios es un poco rara, es por parejas tal como se muestra acontinuacion.

diccionarioEjemplo = {
    "Marca" : "Ford",
    "Modelo" : "Mustang",
    "Anho" : 1955
}
#Para imprimir el valor que me interesa del diccionario hay que guardarlo primero en una variables
datoInteresante = diccionarioEjemplo["Marca"]
print("Juan tiene un auto de marca", datoInteresante)

#Tambien nos podemos recorrer el diccionario con un simple for 
for x in diccionarioEjemplo:
    print(x, ":", diccionarioEjemplo[x])

       
'''Exite un metodo de los diccionarios que nos facilita la lextura en clave y el valor de los elementos, porque 
    devuelve ambos valores en cada iteracion automaticamente'''

for x, y in diccionarioEjemplo.items():
    print(x, ":", y)
    
#Existen tambien las listas anidadas (Vector de Vectores o Listas de Listas en Java)
ListaA = ["Maria", "Carmen", "Joana"]
ListaB = [20, 30, 40]
Resultante = [ListaA, ListaB]

#A la hora de imprimir la variable --> resultante["Esto es la lista que va a usar"]["la posicion de la lista usada "]
print("Juanito quiere a", Resultante[0][0], "que tiene una edad de", Resultante[1][0], "años")

#---------- El sum, como su nombre lo indica, realiza una suma con los numeros que le pasemos, en este caso realizará una suma
# con los numeros que tengamos en el arraylist de numeros y sacara como resultado 15 en este caso ya que es la suma de todos los numeros
#que se encuentran en el array

#Sum sumara aparte de los numeros que tengas en el arraylist, un numero que le pases de paremetro dentro de los parentesis
#un ejemplo puede ser (numeros, 10) numeros es el nombre del arraylist y 10 es el numero externo que sumara aparte
numeros = [1, 2, 3, 4, 5]
resultado = sum(numeros, 10)
print(resultado)
#---------- El sum, como su nombre lo indica, realiza una suma con los numeros que le pasemos, en este caso realizará una suma
# con los numeros que tengamos en el arraylist de numeros y sacara como resultado 15 en este caso ya que es la suma de todos los numeros
#que se encuentran en el array

numeros = [1, 2, 3, 4, 5]
resultado = sum(numeros)
print(resultado)