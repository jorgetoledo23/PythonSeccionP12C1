#Determinar si un alumno aprueba a reprueba un curso, 
# sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 4.0; 
# reprueba en caso contrario.

contador = 1
nota = 0
suma = 0
while contador <=3:
    print("Ingrese Nota N", contador)
    nota = float(input())
    suma = suma + nota
    contador += 1

#print(suma/3)
if suma/3 >= 4.0: 
    print(f"Aprobado con un Promedio de {suma/3}")
    #Otra instruccion
else: print(f"Reprobado con un Promedio de {suma/3}")

