usuario_password= {}
usuario=input("Ingrese su usuario: ")
numero= [0,1,2,3,4,5,6,7,8,9]

a=0
while a<8:
    i=0
    password=[]
    while i<8:
        clave=[]
        consulta= input("Ingrese su password de a 1 caracter: ")
        while len(consulta)!= 1:
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
                
            y= (''.join(password))
            print("Hasta ahora has escrito ", y)
            print(*clave, sep="\n")
        i+1
    if len(clave) ==0:
        print("Su clave está validada")
        break
    else: 
        print("La clave es inválida")
        a+1
    usuario_password[usuario]=y 
for key,value in usuario_password.items:
    print(f"Su usuario es" ,key, "y su contraseña es" ,value)












