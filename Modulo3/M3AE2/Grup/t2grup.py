#se agrega a una variable un mensaje motivador
mensaje = "Mucha suerte en el ejercicio, Cristian, David, Alejandro y Marco"

#mensaje impreso en mayusculas
print (mensaje.upper())

#Muestra que tipo de datos que hay en el mensaje
print ("El tipo de datos es:", type(mensaje))

#se crea una lista con las palabras del String
lista=["Mucha","suerte","en", "el","ejercicio", "Cristian", "David", "Alejandro", "Marco"]
print(lista[:])

#identificar en que parte del indice se encuenta cada integrante en la lista
lista=["Mucha","suerte","en", "el","ejercicio", "Cristian", "David", "Alejandro", "Marco"]
print("Cristian se encuentra en el indice:", lista.index("Cristian"), "de la lista")
print("David se encuentra en el indice:", lista.index("David"), "de la lista")
print("Alenjandro se encuentra en el indice:", lista.index("Alejandro"), "de la lista")
print("Marco se encuentra en el indice:", lista.index("Marco"), "de la lista")

#Indicar cuantas palabras tiene el string
lista=["Mucha","suerte","en", "el","ejercicio", "Cristian", "David", "Alejandro", "Marco"]
print("el string tiene:", len(lista), "palabras")

#Imprimir una tupla con todas las palabras del string
mitupla=tuple(lista)
print(mitupla)

#obtener el mensaje por teclado
input("presione enter para continuar...")
print ("Este es el mensaje obtenido: ",mensaje)
