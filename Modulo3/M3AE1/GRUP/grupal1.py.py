""" Se deberá mostrar en pantalla el total de la suma del pedido el que corresponde al valor neto.
● Se deberá mostrar en pantalla el total del IVA (19%) del total de pedido ingresado.
● Se deberá mostrar en pantalla el total final del pedido (la suma del valor neto + IVA). """

Productos = [["Colchoneta", 20,000],["Mancuernas", 10,000],["Raquetas", 15,000],["Pelotas", 10,000],["Bolsos", 20,000]]

cantprod0 = int(input('¿Qué cantidad quieres de Colchonetas?'))
cantprod1 = int(input('¿Qué cantidad quieres de Mancuernas?'))
cantprod2 = int(input('¿Qué cantidad quieres de Raquetas?'))
cantprod3 = int(input('¿Qué cantidad quieres de Pelotas?'))
cantprod4 = int(input('¿Qué cantidad quieres de Bolsos?'))

Prod0 = Productos[0][1]
Prod1 = Productos[1][1]
Prod2 = Productos[2][1]
Prod3 = Productos[3][1]
Prod4 = Productos[4][1]

totalcol= cantprod0 * Prod0 
totalman= cantprod1 * Prod1
totalraq= cantprod2 * Prod2 
totalpel= cantprod3 * Prod3
totalbol= cantprod4 * Prod4 

valorneto= totalcol + totalman + totalraq + totalpel + totalbol
valoriva= valorneto * 0.19 
valorfinal = valorneto + valoriva

print("valor total pedido: ",valorneto, "valor iva: ", valoriva, "valor final compra: ", valorfinal)