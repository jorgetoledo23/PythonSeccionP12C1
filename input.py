edad = 0
semaforo = False

while semaforo == False:
    try:
        print("Ingresa tu Edad")
        edad = int(input())
        semaforo = True
    except ValueError:
        print("Solo se aceptan valores NUMERICOS")
    except:
        print("Algo salio mal!")
    #Aca FINALIZA EL WHILE

print(f"Ingreso Exitoso. Tu edad es: {edad}")
#print("Ingreso Exitoso. Tu edad es:", edad)

#Tarea: Imprimir por pantalla si es mayor o menor de Edad
    

