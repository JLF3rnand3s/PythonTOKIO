'''La funcion Range() sirve para generar una lista de numeros que podemos recorrer fácilmente, pero no ocupa memoria
porque se interpreta sobre la marcha:'''

for i in range (5):
    '''Explicado de otro modo, el Range() sirve para duplicar
    o repetir algo un numero de veces que le diga el usuario como por ejemplo range(5) --> imprime cinco veces 
    lo siguiente que este dentro del for, ejemplo --> print("hola mundo").
    range en Python es un tipo que se utiliza para representar una secuencia inmutable de números. 
    Uno de sus principales usos es junto a la sentencia for, 
    para definir un bucle sobre el que se itera un número determinado de veces. 
    
    O en palabras simples, te genera una lista de lo que le pases'''
    print("hola mundo")
    
for j in range (3):
    print(j)
    #imprime 0,1,2
  
  #Puedes especificar desde que numero hasta que numero quieres que te muestre  
for h in range(5, 10):
    print(h)
    
'''Range (fin) 1 solo parametro
Range (inicio, fin) 2 parametros
Range (inicio, fin, salto) 3 parametros'''

for k in range (0, 1000, 10):
    print(k)

