#Definir el stock de un producto en una variable.
producto = 50 
#Definir una forma de solicitar el stock disponible del producto por consola.
stockdisp= input("Escribe la letra 's' para conocer nuestro stock disponible: ")

if stockdisp == "s":
    print("stock disponible:", producto, "productos")
else:
    print("caracter no reconocido")

#Definir una forma de solicitar unidades del producto por consola. 
# Este número de productos se almacenarán en una nueva variable llamada ‘Productos seleccionados’.
productos_seleccionados = int(input("¿qué cantidad quieres del producto? "))
print(productos_seleccionados)

producto = producto - productos_seleccionados
print(producto) 
while producto > 0: 
    if productos_seleccionados <= producto:
        if productos_seleccionados > 20:
            print('no se pueden solicitar más de 20 unidades')
            break
        elif productos_seleccionados > 12: 
            productos_seleccionados +=1 
            producto -= productos_seleccionados 
            print('al llevar más de 12 productos te regalamos 1 adicional')
            break
        else :
            producto -= productos_seleccionados 
            print('promoción no válida si llevas menos de 12 productos')
            break

    else: 
        print('falta de stock, producto disponible: ', producto)
    #print(f'falta de stock, producto disponible: {producto}') esta línea tiene el mismo resultado de linea 22, 
    # escrito distinto. 
    break
print('No queda más stock del producto')

""" numero = str(10)
print(type(numero), numero)
texto = "5" 
print(type(texto), texto)
print(numero+texto) """

