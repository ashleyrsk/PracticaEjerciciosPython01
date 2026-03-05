sueldo = float(input("Cuál es tu salario mensual?"))

if sueldo < 1500000:
    print(f" Si tu salario es {sueldo} no pagas impuesto")

if sueldo <= 3000000:
    impuesto = sueldo * 0.5
    sueldo_neto = 3000000 - impuesto    

    print(f"El impuesto correspondiente es {impuesto} y tu salario neto {sueldo_neto}")

        