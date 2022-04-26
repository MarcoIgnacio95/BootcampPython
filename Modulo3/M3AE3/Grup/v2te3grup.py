#Definir el stock de un producto en una variable.
stockproduct= 100

#Definir una forma de solicitar el stock disponible del producto por consola.
stockdisp= input("Escribe la palabra 'stock' para verificar nuestro stock disponible: ")

if stockdisp == "stock":
    print("stock disponible:", stockproduct, "productos")
else:
    print("caracter no reconocido")

#Definir una forma de solicitar unidades del producto por consola. 
# Este número de productos se almacenarán en una nueva variable llamada ‘Productos seleccionados’.
productos_seleccionados = int(input("¿qué cantidad quieres del producto? "))
print(f"has seleccionado: {productos_seleccionados} productos")

#Los productos reubicados serán descontados del stock inicial.
producto = stockproduct - productos_seleccionados
#print(producto) 

#El programa debe verificar que existan unidades disponibles.
if producto > 0:
    print(f"aún tenemos stock disponible: {producto} productos")
else:
    print("no hay stock disponible de este producto")
#Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen más 
# de 12 unidades. Verificar que el stock posibilite entregar una unidad extra. Sino se entregan las unidades justas. 
# Cada una de las posibles acciones debe imprimir un mensaje explicando lo realizado.
#No se pueden solicitar más de 20 unidades en un mismo pedido.
#Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no es posible 
# realizar esta acción debido a que no hay stock suficiente.

