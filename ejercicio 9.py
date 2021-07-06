#suponiendo que me acuerdo bien del ejercicio

from validadorDatos import validarDatoNumerico

def validarDatoBool(mensaje):
    while True:        
        try:
            dato = str(input(mensaje))
            if dato.upper() == "S" or dato == "N":
                break
            else:
                raise Exception
        except:
            print("solo se permite S/N")
    return dato

def validaringrediente(mensaje):
    while True:
        try:
            datoNumerico = int(input(mensaje))
            if datoNumerico in range(0, 7):
                break
            else:
                raise Exception
        except:
            print("Debe ingresar un dato NUMERICO y que este en la lista de ingredientes")
    return datoNumerico

def validarDatoString(mensaje):
    while True:        
        try:
            dato = input(mensaje)
            if dato.isdigit():
                raise Exception
            else:
                break
        except:
            print("solo se permite texto")
    return dato


ing =[]

ingredientes = ["Peperoni (0)", "Queso (1)", "Choclo (2)", "Tomate(3)", "Champiñones (4)", "Tocino (5)", "Salchicha(6)"]

print("-------------------------------- * ------------------------")

print("Bienvenido, arme su pizza, primero escoja la cantidad de ingredientes")
print("1 ingrediente = 3000")
print("2 ingredientes = 4000")
print("3 ingredientes = 5000")
#armar la pizaa
CantIngredientes = validarDatoNumerico("escoja la cantidad de ingredientes que quiere en su pizza \ncada ingrediente adicional tiene un valor de $1500: ")
print("los ingredientes disponibles son:")
if CantIngredientes == 0:
    exit()

for z in ingredientes:
    print(z)

for x in range(1, CantIngredientes+1):
    ing.append(ingredientes[validaringrediente(f"ingrese el ingrdiente N°{x}: ")])
print("su pizza contiene:")
for i in ing:
    print(i)

#agregar otro ingrediente
while True:
    pregunta = validarDatoBool("desea agregar otro ingrediente (S/N): ")
    if pregunta.upper() == "S":
        CantIngredientes += 1
        for x in range(CantIngredientes, CantIngredientes+1):
            ing.append(ingredientes[validaringrediente(f"ingrese el ingrdiente N°{x}: ")])
        print("su pizza contiene ahora:")
        for i in ing:
            print(i)
    else:
        break

#calcular precio

if CantIngredientes < 4:
    precio = 2000 + (1000*CantIngredientes)
    print("el total de su pizza es", precio)

else:
    precio = 5000 + ((CantIngredientes-3)*1000)
    print("el total de su pizza es", precio)

exit()