#Dados dos números enteros, devuelva su producto. Si el producto es mayor que 1000, devuelva su suma

num1 = int(input("Ingrese Numero 1: "))
num2 = int(input("Ingrese Numero 2: "))

producto = num1 * num2
if producto > 1000:
    print(num1 + num2)
else:
    print(producto)

def multipicacion_o_suma(num1, num2):
    producto = num1 * num2
    if producto > 1000:
        return num1 + num2
    else:
        return producto