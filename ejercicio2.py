#Confeccione un algoritmo en diagrama de flujo que, 
# al leer el neto de una factura, 
# calcule el I.V.A. y de cómo salida el total de la factura.

total = 0
neto = 0
iva = 0

print("Ingrese el Valor NETO de la Factura")
neto = int(input())
iva = int(neto * 0.19)
total = int(neto + (neto * 0.19))
print(f"El Total de la Factura es {total}, siendo el valor del IVA: {iva}")
print("El Total de la Factura es", total, ", siendo el valor del IVA:", iva)