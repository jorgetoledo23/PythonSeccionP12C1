#Mostrar el cubo del número hasta un entero dado. (Con Loops)

n = int(input("Ingrese un Numero: "))
for i in range(1, n+1):
    print(f"Numero Actual: {i}, su Cubo es: {i*i*i}")