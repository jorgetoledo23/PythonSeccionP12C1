#Calcule el impuesto sobre la renta para los ingresos dados siguiendo las siguientes reglas
renta = int(input("Ingrese Renta para calular: "))
impuesto = 0
if renta <= 500000:
    impuesto = 0
elif renta >= 500000 and renta <= 1000000:
    impuesto = renta * 0.05
elif renta > 1000000:
    impuesto = renta * 0.07

print(impuesto)