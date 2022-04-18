#Importes
from sys import exit
#Variables
promp = "> "
global maquina
precio_base = input("Precio Base: ")
float_pb = float(precio_base)
tipo_maquina = input("Que tipo de maquina quieres: \n 1.Low Boy\n 2.Big Arcade\n 3.Bartop\n 4.Arcade Pared\n"+promp)

#Variables accesorios



#Funciones
def tipomaquina():
    global maquina
    if tipo_maquina == "1":
        maquina = "Low Boy"
        return maquina
    elif tipo_maquina == "2":
        maquina = "Big Arcade"
        return maquina
    elif tipo_maquina == "3":
        maquina = "Bartop"
        return maquina
    elif tipo_maquina == "4":
        maquina = "Arcade Pared"
        return maquina
    else:
        print("No existe esta configuración.")
        exit(0)

#Funciones accesorios

#Funcion para determinar el  joystick
def joystick():
    global joystick
    joystick_respuesta = input("Selecciona el tipo de joystick que quieres: \n1.Sanwa\n2.Bate Negro\n3.Semi-Pro\n"+promp)
    if joystick_respuesta == "1":
        joystick = 0
    elif joystick_respuesta == "2":
        joystick = 11.50
    elif joystick_respuesta == "3":
        joystick = 57.50
    else:
        print("No seleccionaste ningun joystick")
        exit(0)
    return  joystick
#Funcion para determinar el monitor
def monitor(): #poner para que ponga los precios segun el tamaño que falta
    global maquina
    global monitor
    if maquina == ["Low Boy","Bartop","Arcade Pared"]:
       monitor = input("Selecciona el tamaño de monitor deseado: \n1. 17\'\n2. 19\'"+promp)
       return monitor
    elif maquina == "Big Arcade":
        monitor = input("Selecciona el tamaño de monitor deseado: \n1. 19\'\n2. 22\'"+promp)
        return monitor
    else:
        print("No seleccionaste ningun monitor")
        exit(0)

#Funcion para la marquesina
def marquesina():
    global marquesinas
    respuesta = input("Quieres marquesina:\n1.Si\n2.No\n"+promp)
    if respuesta == "1":
        marquesinas = 23
        
    elif respuesta == "2":
        marquesinas = 0
        
    else:
        print("No seleccionaste ningun tipo de marquesina.")
        exit(0)

#Funcion para el sistema
def sistema():
    global sistema
    respuesta = input("Selecciona el sistema que quieres:\n1.Pandora\n2.Raspberry\n"+promp)
    if respuesta == "1":
        sistema = 0
    elif respuesta == "2":
        sistema = 189.75
    else:
        print("No seleccionaste ningun sistema valido.")
        exit(0)

#Funcion para las ruedas
def ruedas():
    global ruedas
    respuesta = input("Quieres añadir ruedas:\n1.Si\n2.No\n"+promp)
    if respuesta == "1":
        ruedas = 23
        return ruedas
    elif respuesta == "2":
        ruedas = 0
        return ruedas
    else:
        print("No seleccionaste ninguna rueda valida.")
        exit(0)

#Funcion para los armarios
def armarios():
    global armario
    respuesta = input("Quieres añadir armario:\n1.Si\n2.No\n"+promp)
    if respuesta == "1":
        armario = 57.50
        return armario
    elif respuesta == "2":
        armario = 0
        return armario
    else:
        print("No has seleccionado una opcion valida.")
        exit(0)

#Funcion para el monedero
def monedero():
    global monedero
    respuesta = input("Quieres añadir monedero:\n1.Si\n2.No\n"+promp)
    if respuesta == "1":
        monedero = 74.75
        return monedero
    elif respuesta == "2":
        monedero = 0
        return monedero
    else:
        print("No has seleccionado una opcion valida.")
        exit(0)

#Funcion para el posavasos
def posavasos():
    global posavasos
    respuesta = input("Quieres añadir posavasos:\n1.Si\n2.No\n"+promp)
    if respuesta == "1":
        posavasos = 11.50
        return posavasos
    elif respuesta == "2":
        posavasos = 0
        return posavasos
    else:
        print("No has seleccionado una opcion valida.")
        exit(0)





def precios():
    #si es low boy
    if maquina == "Low Boy":
        joystick()
        #monitor()
        marquesina()
        sistema()
        ruedas()
        armarios()
        monedero()
        posavasos()
        print("El total es: "+float_pb+joystick+sistema+marquesinas+ruedas+armario+monedero+posavasos) #falta poner el monitor
        #print(float_pb+joystick+sistema+marquesina+ruedas+armario+monedero+posavasos)

    elif maquina == "Big Arcade":
        "a"
        #joystick
        #monitor 19/22
        #marquesina
        #sistema
        #ruedas
        #armario
        #monedero
        #posavasos
    elif maquina == "Bartop":
        "a"
        #joystick
        #Monitor
        #Marquesina
        #Sistema
    elif maquina == "Arcade Pared":
        "a"
        #Joystick
        #Monitor
        #Sistema
    else:
        "a"

if __name__ == "__main__":
    tipomaquina()
    precios()
    #print(precio_base+joystick+monitor+sistema+marquesina+ruedas+armario+monedero+posavasos)
