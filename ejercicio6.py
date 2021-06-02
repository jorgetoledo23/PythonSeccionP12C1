#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
#Si trabaja 40 horas o menos se le paga $1600 por hora
#Si trabaja más de 40 horas se le paga $1600 por cada una de las primeras 40 horas y $2000 por cada hora extra.

from validadorDatos import validarDatoNumerico

horasTrabajadas = validarDatoNumerico("Ingrese cantidad de horas trabajadas: ")

if horasTrabajadas <= 40:
    horasNormales = horasTrabajadas
    horasExtras = 0
else:
    horasNormales = 40
    horasExtras = horasTrabajadas - 40 # 50 - 40 = 10 horasExtras

totalPagar = (horasNormales * 1600) + (horasExtras * 2000)
print(f"Total a Pagar: {totalPagar}")