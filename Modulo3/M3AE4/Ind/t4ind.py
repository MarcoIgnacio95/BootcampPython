#Nuestra aplicación tendrá la siguiente particularidad. Al momento de crear un usuario, este debe ingresar 
# una contraseña que esté acorde a nuestros criterios de seguridad.
#En este sentido, la contraseña debe contar con al menos 8 caracteres, con mayúsculas, minúsculas y cifras.
#Nuestro programa debe indicarle al usuario qué criterios le faltan para disponer de una contraseña segura.
#La contraseña debe ingresarse carácter por carácter en el terminal. Luego de escribir cada carácter, el 
# programa envía un mensaje con los criterios aún incumplidos.


usuario_contraseña= {}
usuario=input("Ingrese su usuario: ")
numero= [0,1,2,3,4,5,6,7,8,9]

a=0
while a<8:
    i=0
    password=[]
    while i<8:
        clave=[]
        consulta= input("Ingrese su password de a 1 caracter: ")
        while len(consulta) != 1:
            print("Debe ingresar nuevamente su password, de a 1 caracter, por favor")
            consulta=input("Sólamente de a 1 caracter: ")
        else:
            password.append(consulta)
            if len(consulta)!=1:
                consulta=input("Ingrese sólo un caracter: ")
            else: 
                if len(password) <8:
                    clave.append("Su password debe tener al menos 8 caracteres")
                if not any(char.islower() for char in password):
                    clave.append("Su password debe tener al menos una letra minúscula")
                if not any(char.isupper() for char in password):
                    clave.append("Su password debe contener al menos una letra mayúscula")
                if not any(char.isdigit() for char in password):
                    clave.append("Su password debe tener al menos un número")
            x= (" ".join(password))
            print("Hasta ahora has escrito ", x)
            print(*clave, sep="\n")
        i+1
    if len(clave) ==0:
        print("Su clave está validada")
        break
    else: 
        print("La clave es inválida")
        a+1
    usuario_contraseña[usuario]=x 
for key,value in usuario_contraseña.items:
    print(f"Su usuario es" ,key, "y su contraseña es" ,value)












