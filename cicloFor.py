frutas = ["Manzana", "Cereza", "Pera"]
print(frutas[1])

for fruta in frutas:
    print(fruta)

autos = ["Mazda","Citroen", "Audi", "Mercedez Benz"]
for auto in autos:
    print(auto)

for letra in "Auto":
    print(letra)

encontrado = False
for auto in autos:
    print(auto)
    if auto == "Citroen":
        encontrado = True
        break

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

#Comienzo, Termino, Incremento
#              C, T, I
for x in range(2, 6, 2):
    print(x)
    
