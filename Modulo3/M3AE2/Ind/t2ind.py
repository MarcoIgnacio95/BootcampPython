#Creo el string con los usuarios

usuarios= "Pedro,Miguel,Angela,Ana,José,Daniela,Karen"

#Transformo la tupla en lista. 
listausuarios= usuarios.split(',') #obs: la coma del comando actúa como delimitador. 
print(listausuarios) #La tupla no se modifica.

print("Total de usuarios registrados: ", len(listausuarios)) #usuarios es el string, listausuarios es la lista.

print("Nombre de usuario: ")
nombre= input()

#Aplicar for, que es un tipo de ciclo. 

for f in listausuarios: 
    if nombre == f: 
        print('Hola', f)

print("-------------------------------------------")
for k in listausuarios:
    print('Hola', k)