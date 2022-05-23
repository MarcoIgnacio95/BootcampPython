
#Diseñe 7 diccionarios, donde el nombre de cada diccionario es el nombre de un usuario de su aplicación.
#En cada diccionario, integre características como: edad, género y otras características particulares de 
# su aplicación.
#Por ejemplo, si la aplicación se enfoca en Juntas de Vecinos integrar dirección y número telefónico. 
# Integre al menos cinco características.
#Guarde estos diccionarios en una lista. En el caso de ejemplo, podría ser nombrada “JJVV”.
#A continuación, recorra su lista e imprima toda la información que posee la estructura de datos sobre 
# cada usuario (en el caso de ejemplo: de cada junta de vecinos).
#¿Qué problemas encontró con esta forma de almacenar la información?
#Vuelva al inicio del problema y diseñe una estructura de datos unificada que permita almacenar todas las juntas 
# de vecinos.
#Agregue para cada usuario los campos nombre_usuario, id_unico, antigüedad, fecha de incorporación.
#Imprima en pantalla la fecha de incorporación de todos los usuarios.



''' 
clientes = []

usuario1 = {
    "nombre": "Ernesto",
    "edad": 24,
    "genero": "masculino",
    "comuna": "Lo Prado",
    "celular": "+569 81452938",
    "direccion": "Los pastores 24"
}

usuario2 = {
    "nombre": "Pedro",
    "edad": 41,
    "genero": "masculino",
    "comuna": "Chiloé" ,
    "celular": "+569 45873621",
    "direccion": "Los patos 253"
}

usuario3 = {
    "nombre": "Susana",
    "edad": 21,
    "genero": "femenino",
    "comuna": "Punta Arenas" ,
    "celular": "+569 89732015",
    "direccion": "Gales 245"
}

usuario4 = {
    "nombre": "María",
    "edad": 32,
    "genero": "femenino",
    "comuna": "Valparaíso" ,
    "celular": "+569 75321495",
    "direccion": "Los leones 785"
}

usuario5 = {
    "nombre": "José",
    "edad": 50,
    "genero": "masculino",
    "comuna": "Los Andes" ,
    "celular": "+569 47321685",
    "direccion": "Alamo blanco 2435"
}

usuario6 = {
    "nombre": "Francisca",
    "edad": 52,
    "genero": "femenino",
    "comuna": "San Miguel" ,
    "celular": "+569 54132485",
    "direccion": "Pintores 124"
}

usuario7 = {
    "nombre": "Angélica",
    "edad": 19,
    "genero": "femenino",
    "comuna": "Antofagasta" ,
    "celular": "+569 32168759",
    "direccion": "Las poetas 4253"
}
'''
#clientes.append(usuario3)
#clientes.append(usuario2)
#clientes.append(usuario4)
#clientes.append(usuario5)
#clientes.append(usuario1)
#clientes.append(usuario6)
#clientes.append(usuario7)

#print(clientes)

#El problema de almacenar la información de esta manera, es que se guarda de manera desordenada, y se visualizan 
# los datos del diccionario, pero no se asocia a los nombres del diccionario, en este caso, a los clientes.




clientes = {
    "usuario1" :{
    "nombre": "Ernesto",
    "edad": 24,
    "genero": "masculino",
    "comuna": "Lo Prado",
    "celular": "+569 81452938",
    "direccion": "Los pastores 24",
    "fecha de incorporación":"15,03,2022",
    },
    "usuario2" : {
    "nombre": "Pedro",
    "edad": 41,
    "genero": "masculino",
    "comuna": "Chiloé" ,
    "celular": "+569 45873621",
    "direccion": "Los patos 253",
    "fecha de incorporación":"27,05,2011",
    },
    "usuario3" : {
    "nombre": "Susana",
    "edad": 21,
    "genero": "femenino",
    "comuna": "Punta Arenas" ,
    "celular": "+569 89732015",
    "direccion": "Gales 245",
    "fecha de incorporación":"27,08,2020",
    },
    "usuario4" : {
    "nombre": "María",
    "edad": 32,
    "genero": "femenino",
    "comuna": "Valparaíso" ,
    "celular": "+569 75321495",
    "direccion": "Los leones 785",
    "fecha de incorporación":"10,07,2015",
    },
    "usuario5" : {
    "nombre": "José",
    "edad": 50,
    "genero": "masculino",
    "comuna": "Los Andes" ,
    "celular": "+569 47321685",
    "direccion": "Alamo blanco 2435",
    "fecha de incorporación":"30,03,2007",
    },
    "usuario6" : {
    "nombre": "Francisca",
    "edad": 52,
    "genero": "femenino",
    "comuna": "San Miguel" ,
    "celular": "+569 54132485",
    "direccion": "Pintores 124",
    "fecha de incorporación":"19,10,2009",
    },
    "usuario7" : {
    "nombre": "Angélica",
    "edad": 19,
    "genero": "femenino",
    "comuna": "Antofagasta" ,
    "celular": "+569 32168759",
    "direccion": "Las poetas 4253",
    "fecha de incorporación":"17,12,2021",
    },
}


for cliente in clientes:
    print(cliente)


