edad = int(input("Ingrese su edad: "))
estrato = int(input("Ingrese su estrato"))

if (edad >= 18 and edad <= 25) and (estrato >= 1 and estrato <= 3):
    print ("Aplica para subsidio")
else:
    print("No aplica subsidio")
