def validarDatoNumerico(mensaje):
    while True:
        try:
            datoNumerico = int(input(mensaje))
            break
        except:
            print("Debe ingresar un dato NUMERICO!")
    return datoNumerico

def validarDatoString(mensaje):
    dato = input(mensaje)
    return dato

def validarRut(Rut):
    #Validador de Rut
    rutValidado = False
    return rutValidado