#Escribe una función llamada calcularPotencia(base, exp) que devuelva un valor int de base aumentada 
# a la potencia de exp.

def calcularPotencia(base, exp):
    num = exp
    resultado = 1
    while num > 0:
        resultado = resultado * base
        num = num - 1
    return resultado 

def calcularPotencia2(base, exp):
    resultado = 1
    for i in range(exp):
        resultado = resultado * base
    return resultado 

print(calcularPotencia2(2, 3))