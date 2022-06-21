#####Actualizar valores en diccionarios y listas#####
#1.)  Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15 # selecciona la segunda llave que es: [10,8,9] y el primer[0]valor de la llave que es[10], resultado [[5, 2, 3], [15, 8, 9]]
print("soy X",x)
print("-------------------------------")


#2.)Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print("Soy Estudiante",estudiantes[0]['last_name'])                     #aca seleccionamos de la lista estudiantes[0](que viene siendo:{'first_name':  'Michael', 'last_name' : 'Jordan'},)con la tabla de la lista 1 que es:['last_name']
estudiantes[0]['last_name'] = 'bryant'                                  # aca cambiamos el nombre de la lista.
print("FINAL, Soy Estudiante Actualizado",estudiantes[0]['last_name'])  # imprimimos



#3.)En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
print("SOY EL DEPORTE",directorio_deportes['fútbol'][0])
directorio_deportes['fútbol'][0] = 'Andres'
print("FINAL SOY EL DEPORTE",directorio_deportes['fútbol'][0])



#4 Cambia el valor 20 en z a 30.
z = [ {'x': 10, 'y': 20} ]
print("CAMBIAR EL VALOR Z",z[0]['y'])
z[0]['y'] = '30'
print("FINAL CAMBIAR EL VALOR Z",z[0]['y'])
print("-------------------------------")



##### Iterar a través de una lista de diccionarios #####
#1.) Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada 
# diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for clave in estudiantes:                   # creamos el bucle for que repite la funcion hasta finalizar
    for llave,valor in clave.items():       # creamos otro bucle que al recorrer el diccionario
        print(f"RECORRER LOS ESTUDIANTES llave: {llave}, y valor: {valor}") # luega me imprima el valor. 
    #print(f"Dict:{clave}")
print("-------------------------------")




##### Obtener valores de una lista de diccionarios #####
#1.)Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, 
# iterateDictionary2('name', estudiantes) debería generar:


estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
indice = 0                                  # creamos un indice
while indice < len(estudiantes):            # usamos un bucle while que va a controlar la variable INDICE
    print(estudiantes[indice]['first_name'])
    indice += 1                             # #incrementamos el índice en una unidad
#salida
#Jordan
#Rosales
#Guillen
#Tonel
print("-------------------------------")




########## Y iterateDictionary2('last_name', estudiantes) debería generar:#################
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
indice = 0 # creamos un indice
while indice < len(estudiantes): # usamos un bucle while que va a controlar la variable INDICE
    print(estudiantes[indice]['last_name'])
    indice += 1 # #incrementamos el índice en una unidad
#salida
#Jordan
#Rosales
#Guillen
#Tonel
print("-------------------------------")


########## Iterar a través de un diccionarios con valores de lista #################
#1.) Crea una función printInfo(some_dict)que, dado un diccionario 
# cuyos valores son todos listas, imprima el nombre de cada clave 
# junto con el tamaño de su lista, y luego imprima los valores 
# asociados dentro de la lista de cada clave. Por ejemplo:

def printInfo(some_dict): # creamos la funcion
    print(len(dojo['ubicaciones']), "UBICACIONES")# imprimimos la longitud del diccionario
    for ubicacion in dojo['ubicaciones']:# creamos un bucle for para recorrer los elementos
        print(ubicacion)
    print("-------------------------")
    print(len(dojo['instructores']), "INSTRUCTORES")
    for instructor in dojo['instructores']:
        print(instructor)

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
   
}
printInfo(dojo)
# salida:
"""7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
#
"""