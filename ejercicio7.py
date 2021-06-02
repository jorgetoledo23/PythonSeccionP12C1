#Crear un algoritmo que permita leer n números y determinar cuál fue el mayor 
#ingresado y, cuál el menor.

#from validadorDatos import *
import validadorDatos as vD

cantidadNumeros = vD.validarDatoNumerico("Ingrese Cantidad de Numeros: ")
menor = 0
mayor = 0

for n in range(1, cantidadNumeros + 1): # 10, 20
    num = input(f"Ingrese numero {n}: ")
    if n == 1:
        mayor = num
        menor = num
    else:
        if num < menor:
            menor = num
        if num > mayor:
            mayor = num
            
print(f"El numero Menor es {menor} y el Mayor es {mayor}")