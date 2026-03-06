usuario = input ("Ingrese su nombre de usuario")
contraseña = int(input("Ingrese su contraseña"))

if usuario == "admin" and contraseña == 1234:
    print("Permitido el acceso")

else:
    print("Acceso denegado")
    