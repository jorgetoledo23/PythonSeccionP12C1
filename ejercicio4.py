#Crear un algoritmo en diagrama de flujo que pida al usuario 
# la cantidad de hijos que este tiene. 
# Si es que tiene hijos entonces que ingrese la edad de cada uno 
# y asignar un bono de $25.000 por cada hijo de entre 3 y 15 años. 
# Al final mostrar el total de dinero que obtendría en bono

cantHijos = int(input("Ingrese cantidad de hijos: "))
totalBono = 0
for hijo in range(1, cantHijos+1):
    edad = int(input(f"Ingrese la edad del Hijo N{hijo}: "))
    if edad >= 3 and edad <= 15:
        totalBono += 25000
    else: print("Este hijo no tiene derecho a BONO.")
print(f"Total a Pagar: {totalBono}")
