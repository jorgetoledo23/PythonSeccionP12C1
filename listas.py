#Ingresar n cantidad de numeros y devolverlos ordenados de manera ascendente (de menor a mayor)
from validadorDatos import validarDatoNumerico

listNumeros = []

cantidadNumeros = validarDatoNumerico("Ingrese cantidad de Numeros: ")

for i in range(1, cantidadNumeros + 1):
    num = validarDatoNumerico(f"Ingrese numero {i}: ")
    listNumeros.append(num)

print(listNumeros)
listNumeros.sort()
print(listNumeros)
#index = Posicion de un Elemento dentro de la Lista
listNumeros.pop(0)
listNumeros.remove(123)
print(listNumeros)
print(listNumeros[0])
listNumeros.sort(reverse=True)
print(listNumeros)

for n in listNumeros:
    print(n)
    