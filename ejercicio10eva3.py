#Escriba una función que reciba dos parámetros, 
# nombre y sueldo bruto de un empleado. 
# Aplicar los descuentos de salud (7%) y previsión (12%) al sueldo. 
# Para finalizar imprima, por ejemplo:
def calculoSalario(nombre, sueldo):
    sueldo = sueldo * 0.81
    print(f"El Empleado {nombre}, recibe un total de: ${sueldo}")


calculoSalario("Jorge", 500000)