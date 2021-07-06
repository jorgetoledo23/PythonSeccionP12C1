#Dado un rango de los primeros 10 números, Itere desde el número inicial hasta el número final, y en cada iteración 
# imprima la suma del número actual y el número anterior. (Con Loops)

for i in range(11):
    if i == 0:
        print(f"Numero Actual: {i} Numero Anterior {i} Suma: {i}")
    else:
        print(f"Numero Actual: {i} Numero Anterior {i-1} Suma: {i + (i-1)}")
