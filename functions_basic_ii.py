#PRIMER EJERCICIO
"""
Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que 
cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]


listaa = int(input("Dígame un numero: "))# Creamos el input donde acepte el numero
def createList(n): #creamos la funcion de la lista (parametro)
    lista = [] # agregamos la variable de la lista, donde se guardara los numeros
    for i in range(n,-1, -1): # definimos la funcion que va efectuar 
        lista.append(i) # imprimo la lista y le agregamos un digito al final
    return(lista)# retorna el valor de la lista
print(createList(listaa)) #imprime el resultado."""

#SEGUNDO EJERCICIO
"""
Imprimir y devolver: crea una función que reciba una lista con dos números. 
Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

x = str(input("Dígame recibe numero uno: "))
print(x[:-6])
# la salida sería [99,4,2,5,-3]
print(x[2:-4])
# la salida sería [4,2,5,-3];
print(x[4:-2])
# la salida sería [99,4,2,5]
print(x[6:])
# la salida sería [2,5];
#salida
# se escribe asi: 5,6,8,7
#resultado:
#5
#6
#8
#7
print()
"""

#TERCER EJERCICIO
"""Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer 
valor de la lista, más la longitud de la lista. Ejemplo: primero_mas_longitud([1,2,3,4,5]) 
debe devolver 6 (primer valor: 1 +length: 5)

def createList(lista):
    listaa = []
    for letra in lista[1::2]:
        listaa.append(int(letra))
    return listaa
def operar(lista):
    image = lista[0] + len(lista)
    return image


texto = input("ingresa tu lista: ")
lista = createList(texto)
final = operar(lista)
print(final)
"""
#CUARTO EJERCICIO
"""
Valores mayores que el segundo: escribe una función que acepte una 
lista y cree una nueva que contenga solo los valores de la lista 
original que sean mayores que su segundo valor. Imprime cuántos 
valores son y luego devuelve la lista nueva. Si la lista tiene 
menos de 2 elementos, has que la función devuelva False

Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe 
imprimir 3 y devolver [5,3,4]

Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
"""

"""def nueva_lista_2(lista):
    listaa = []
    for i in lista:
        if i in lista[1::2]:
            listaa.append(i)
            print("soy una segunda lista: ",i)
    return listaa

def operar(lista):
    listaa = nueva_lista_2
    print("esto es el Operar")

texto = input("Ingrese una lista: ")
lista = nueva_lista_2(texto)
final = operar(lista)
print("Hola soy el final del texto", final)

"""




"""def nuevalista(lista):
    nueva_lista = []
    print("Hola nueva lista",nueva_lista)
    for i in lista:
        print("Hola nueva lista con for",lista)
        if i nueva_lista[0:1] > lista == 2:
            nueva_lista.append(i)
            print("Hola nueva lista con if",lista)
        else:
            print("no es interador")
    return lista

def operar(lista):
    image = lista > lista
    return image

texto = input("Ingresa la Lista: ")
lista = nuevalista(texto)
final = operar(lista)
print(final)
"""


"""
texto = input("Ingresa la Lista: ")
def nuevalista(lista):
    arreglo = []
    for i in lista:
        if i > 2 != 0:
            arreglo.append(i)
    return arreglo
lista = nuevalista(texto)
print(nuevalista(texto))
print("Esta lista es la original",texto)"""


# ! Countdown - Cree una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás de uno en uno, desde el número 
# (como elemento 0) hasta 0 (como último elemento).

def countdown(num): 
    output = [] 
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(countdown(5))
"""# ? Example: countdown(5) should return [5,4,3,2,1,0]

# ! Imprimir y devolver: 
# crea una función que recibirá una lista con dos números. Imprime el primer valor y devuelve el segundo.

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))
# ? Example: print_and_return([1,2]) should print 1 and return 2


# ! ! Primero más longitud: cree una función que acepte una lista y 
# devuelva la suma del primer valor de la lista más la longitud de la lista.
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))
# ? Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


# ! Valores mayores que el segundo: escriba una función que acepte una lista y 
# cree una nueva lista que contenga solo los valores de la lista original que sean 
# mayores que su segundo valor. Imprima cuántos valores es esto y luego devuelva la nueva lista. 
# Si la lista tiene menos de 2 elementos, haga que la función devuelva Falso

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# ? Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# ? Example: values_greater_than_second([3]) should return False

# ! Esta longitud, ese valor: escriba una función que acepte dos números enteros como parámetros: 
# tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado 
# y cuyos valores sean todos los valores dados.

def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
# ? Example: length_and_value(6,2) should return [2,2,2,2,2,2]"""