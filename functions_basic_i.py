#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#salida: retorna 5 ya que se le esta dando un valor al returno
# 5
print()#salto de linea

"""
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#salida
#error, ya que no esta definida la variable.
"""


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#salida
#retorna el 5 ya que imrpime solo el primer retorno de la funsion.
print()#salto de linea


#4
def number_of_fingers():
    print(10)
    return 5
    
print(number_of_fingers())
#salida
#imrprime solo el numero 5, ya que el print(10) esta del retur y no es posible imprimir
print()#salto de linea



#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Solucion
#5
#none en el otro print(x) porque no hay ningu parametro que enviar-
print()#salto de linea


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#solucion:
#3
#5
#print(add(1,2) + add(2,3)) imrpime la sumatoria de (1+2)=3 (2+3)= 5 
print()#salto de linea


#7
def concatenate(b,c): #declaramos la funcion
    return str(b)+str(c)# retornamos la sumatoria de los 2 estring
print(concatenate(2,5)) # imprime el resultado de 25, ya que concatena los dos digitos
#solucion
#25
print() #salto de linea

#8
def number_of_oceans_or_fingers_or_continents():# definimos la funcion
    b = 100 # declaramos la variable
    print(b) #imprimimos 100
    if b < 10: # si 100 < 10:
        return 5 # retornar 5 en caso de que 100 sea mayor que 10
    else: #sino se cumple el if de b < 10
        return 10 # retornamos 10
    return 7 # este retorno no se imprime ya que se cumple la condicion del return 10
print(number_of_oceans_or_fingers_or_continents()) # imrpime el 100 y el 10 que es el retur 10
#solucion
#100
#10
print() #salto de linea

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))#21 ya que suma 7 + 14= 21
#solucion
#7
#14
#21
print()#salto de linea


#10
def addition(b,c):# delcara la funcion
    return b+c #retorna la sumatoria de 3+5=8
    return 10 
print(addition(3,5))# salida 8 la sumatoria de los dos argumentos
#Solucion
#8 retorna ya que 
print()#salto de linea


#11
b = 500
print("este es1 ",b)
def foobar():
    b = 300
    print(b)
print("este es2 ",b)# imrpime 500 ya que imprime lo que esta fuera de la funcion. y agregado en la variable b
foobar()# imprime el resultado dentro de la funcion. que son 300
print("este es3 ",b)# imrpime 500 ya que imprime lo que esta fuera de la funcion. y agregado en la variable b
#salida
#500
#500
#300 que es la impresion del segundo foobar() el cuale sta dentro de la funcion foobar
#500
print()#salto de linea



#12
b = 500
print("1",b) #1 500
def foobar():
    b = 300     
    print("3",b)#2 300    
print("2",b)#4 500
foobar()
print("4",b)#5 500
#salida
#500 primero imprime la variable b= 500
#500 segundo imprime "2",b
#300 
#500
print()#salto de linea


#13
b = 500
print("1",b)
def foobar():
    b = -300
    print("3",b)
    return b
print("2",b)
b=foobar()
print(" imprime el resultado de la variable b=foobar 4",b)
#Salida
#500
#500
#300
#300
print()#salto de linea

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#salida
#1
#3
#2
print()#salto de linea

#15
def foo():
    print(1)# primero impresion
    x = bar()
    print(x)
    return 10 # cuarta impresion
def bar():
    print(3)# segunda impresion
    return 5 # tercera impresion
y = foo()
print(y)
#salida
#1
#3
#5
#10

"""
# resultados desde la plataforma
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) 
# ! >>> 5

#2
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# ! >>> undefined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# ! >>> 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# ! >>> 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# ! >>> 5 , None

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# ! >>> 3, 5,Error can't add NoneTypes

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# ! >>> "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# ! >>> 100, 10
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# ! >>> 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# ! >>> 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# ! >>> 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# ! >>> 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# ! >>> 500,500, 300, 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# ! >>>> 500, 500, 300, 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# ! >>> 500, 500, 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# ! >>> 1, 3, 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# ! >>> 1, 3, 5 , 10

"""




