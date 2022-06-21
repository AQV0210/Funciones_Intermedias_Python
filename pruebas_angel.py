"""
Esta funcion, colocas un numero y resta el numero indicado -1.
"""
"""listaa = int(input("Dígame un numero: "))
def crearlistanumero(n):
    lista = []
    for i in range(n):
        lista.append([])
    return(i)
print(crearlistanumero(listaa))"""

#DICCIONARIOS
"""dic_vacío = {}
new_person = {'name': 'John', 'edad': 38, 'peso': 160.2, 'usa_lentes': False}
new_person['name'] = 'Jack'	# actualiza si la llave existe, agrega un par clave-valor si no
new_person['hobbies'] = ['escalada', 'programación']
print("primer prin",new_person)	
# salida: {'name': 'Jack', 'edad': 38, 'peso: 160.2, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}
w = new_person.pop('peso')	# remueve la llave indicada y devuelve el valor
print("segundo prin",w)		# salida: 160.2
print("tercer prin",new_person)	
# salida: {'name': 'Jack', 'edad': 38, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}        .

#LISTAS
lista_vacía = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# salida: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# salida: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# salida: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# salida: ['Francis', 'Oliver'

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

#PATRA UTILIZAR NUMEROS ALEATORIOS
from ossaudiodev import SOUND_MIXER_BASS
import random
from tkinter import N
print(random.randint(2,5)) # proporciona un número aleatorio entre 2 y 5

#CONCANETAR
name = "Zen"
print("Mi nombre es " + name)
print()
#utilizando F
name = 'Angel'
print(f"Mi nombre es {name}")
print()
#coversion de tipos
print("Hola" + str(42))# salida: Hola 42
print()


#INTERPOLACION DE CADENAS
first_name = "Angel"
last_name = "quintero"
age = 27
print(f"Mi nombre is {first_name} {last_name} and tengo {age} años de edad.")
print()

#%-formatting
# % para indicar un parametro
#%s para indicar una cadena
#%d para un numero
hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3
print(hw, py)
name = "Zen"
age = 27
print("Mi nombre es %s y tengo %d" % (name, age))
print()

#METODOS DE CADENA INTEGRADOS
x = "hola mundo!"
v = "es el año : %d" % 2022
print(x,v)
# salida:
#print(x.upper()) : Imprime en MAYUSCULA
#print(x.lower()): Imprime en miniscula
#print(x.count(str())): Imprime el valor de caracteres incluyendo espacio + 1
#print(v.join(x)) : Devuelve una lista concatenada
#"Hola Mundo"
print()

#LISTAS
ninjas = ['Rozen', 'KB', 'Oliver']
mi_lista = ['4', ['lista', 'en', 'una', 'lista'], 987]
lista_vacía = []
print(mi_lista)
print()

#LISTAS DENTRO DE UNA LISTA
frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
ensalada = 3 * vegetales
print(ensalada)
print()

#COMO ACCEDER A LOS VALORES DE UNA LISTA
"""
"""Supongamos que tenemos un cajon, donde el indice 0 es 'documento', el indice 1 es 'sobres' y el indice 2 es 'lapices'
"""
"""
cajón = ['documentos', 'sobres', 'lápices']
# acceder al cajón con índice 0 y valor print
print(cajón[0])  # imprime documentos
# acceder al cajón con índice 1 y  valor print
print(cajón[1]) # imprime sobres
# acceder al cajón con índice 2 y valor print
print(cajón[2]) # imprime lápices


#FUNCION PARA MANIPULAR LISTAS
x = [1,2,3,4,5]
x.append(99)
print(x)
# la salida sería [1,2,3,4,5,99]
print()


#otro Ejemplo de maipular LISTAS
x = str(input("Dígame recibe numero uno: "))
print(x[:1])
# la salida sería [99,4,2,5,-3]
print(x[1:])
# la salida sería [4,2,5,-3];
print(x[:4])
# la salida sería [99,4,2,5]
print(x[2:4])
# la salida sería [2,5];
"""

"""x = str(input("Dígame recibe numero uno: "))
print(x[:1])
# la salida sería [99,4,2,5,-3]"""

#Dígame recibe numero uno: 1.1
#[1]
#[2, 3, 4, 5, 99]
#[1, 2, 3, 4]
#[3, 4]

"""
#######Prueba de coder:############

Imprimir y devolver: crea una función que reciba una lista con dos números. 
Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

x = str(input("Dígame recibe numero uno: "))
print(x[2:3])
# la salida sería [99,4,2,5,-3]
print(x[4:5])
# la salida sería [4,2,5,-3];
print(x[6:-4])
# la salida sería [99,4,2,5]
print(x[8:-2])
# la salida sería [2,5];
#salida
# se escribe asi: ([5,6,8,7])
#resultado: 
'''
5
6
8
7
"""
"""import math
def hipotenusa(numeros):
    for suma in sumar:
        suma = entrada + suma
    return sumar

entrada = input("ingresa el numero: ")
numeros = hipotenusa(entrada)
sumar = numeros
final = sumar
print("Este es el resultado",final(math.sqrt(10)))"""

"""def algoritmos(numeros):
    variable = []
    for inicio in sumar(5,6):
        if inicio >= 18:
            print(inicio)
        else:
            print("no eres")
        return inicio

print("fin del algoritmo: ")"""


