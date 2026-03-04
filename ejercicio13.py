precio = float(input ("cuál es el precio del producto?"))

if precio > 100000:
    precio_final = precio -(precio*0.10)
    print(f"EL valor a pagar es : ${precio_final}")
else:
    print(f"El valor a pagar es: $ {precio}")
