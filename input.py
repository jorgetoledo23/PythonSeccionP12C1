edad = 0
bandera = False

while bandera == False:
    try:
        print("Ingresa tu Edad")
        edad = int(input())
        bandera = True
    except ValueError:
        print("Solo se aceptan valores NUMERICOS")
    except:
        print("Algo salio mal!")
print(f"Ingreso Exitoso. Tu edad es: {edad}")
#print("Ingreso Exitoso. Tu edad es:", edad)

#Tarea: Imprimir por pantalla si es mayor o menor de Edad
    

