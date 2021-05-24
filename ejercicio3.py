#Determinar si un alumno aprueba a reprueba un curso, 
# sabiendo que aprobara si su promedio de x cantidad de calificaciones es mayor o igual a 4.0; 
# reprueba en caso contrario.

print("Bienvenido al Sistema de Promedios de la Clase de Python...")
cantidadNotas = int(input("Por Favor, Ingresa la Cantidad de Notas que deseas calcular como Promedio: "))
suma = 1
for x in range(1, cantidadNotas + 1):
    nota = int(input(f"Ingrese nota {x}: "))
    suma += nota
promedio = int(suma / cantidadNotas)
if promedio >= 4: print(f"Aprobado con un Promedio de {promedio}")
else: print(f"Reprobado con un Promedio de {promedio}")


        