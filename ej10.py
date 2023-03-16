class Habitacion():
    def __init__(self, largo, ancho, ventanas, puertas):
        self.__largo=largo
        self.__ancho=ancho
        self.__ventanas=ventanas
        self.__puertas=puertas
        self.__color="blanco"
        self.__esdorm=False

    def set_largo(self, largo):
        self.__largo=largo
    def set_ancho(self, ancho):
        self.__ancho=ancho
    def set_ventanas(self, ventanas):
        self.__ventanas=ventanas
    def set_puertas(self, puertas):
        self.__puertas=puertas
    def pintar(self, color):
        self.__color=color
    def set_esdorm (self, esdorm):
        self.__esdorm=esdorm


    def get_largo(self):
        return self.__largo
    def get_ancho(self):
        return self.__ancho
    def get_ventanas(self):
        return self.__ventanas
    def get_puertas(self):
        return self.__puertas
    def get_color(self):
        return self.__color
    def get_esdorm (self):
        return self.__esdorm
    

class Dormitorio(Habitacion):
    def __init__ (self, camas, largo, ancho, ventanas, puertas):
        self.__camas=camas
        super().__init__(largo, ancho, ventanas, puertas)
    def set_camas (self, camas):
        self.__camas=camas
    def get_camas (self):
        return self.__camas
        


def datos_hab(lista):
        largo=input("Introduzca el largo de la habitación (EN METROS):")
        ancho=input("Introduzca el ancho de la habitación (EN METROS):")
        ventanas=input("Introduzca el número de ventanas que tiene la habitación:")
        puertas=input("Introduzca el número de puertas que tiene la habitación:")
        preg=input("¿Desea pintar la habitación? Introduzca 1 para SÍ, o introduzca 2 para NO:")

        if preg=="1":
            color=input("Introduzca el color del que quiera pintar la habitación:")
            miHabitacion=Habitacion(largo, ancho, ventanas, puertas)
            miHabitacion.pintar(color)
        elif preg=="2":
            print ("Ha decidido no pintar la habitación, por lo que se quedará de color blanco.")
            miHabitacion=Habitacion(largo, ancho, ventanas, puertas)
        else:
            print ("Dato introducido no válido.")
        
        extra=input("¿La habitación es un dormitorio? Introduzca 1 para SÍ, o introduzca 2 para NO:")
        if extra=="1":
            camas=input("Introduzca el número de camas que tiene el dormitorio:")
            global miDormitorio
            miDormitorio=Dormitorio(camas, largo, ancho, ventanas, puertas)
            miDormitorio.set_esdorm(True)
            lista.append(miDormitorio)
        elif extra=="2":
            miHabitacion=Habitacion(largo, ancho, ventanas, puertas)
            lista.append(miHabitacion)
        else:
            print ("Dato introducido no válido.")



def eliminar_hab(lista):
    print ("Introduzca ")



def modificar_hab(lista):
    print ("Introduzca ")



def fin_programa(lista):
    print ("Ha decidido finalizar el programa.")
    for x in range (0, len(lista)):
        print ("Esta habitación tiene", (lista[x].get_largo()), "metros de largo.")
        print ("Esta habitación tiene", (lista[x].get_ancho()), "metros de ancho.")
        print ("Esta habitación tiene", (lista[x].get_ventanas()), "ventanas.")
        print ("Esta habitación tiene", (lista[x].get_puertas()), "puertas.")
        print ("Esta habitación está pintada de color", (lista[x].get_color()),".")
        if miDormitorio.get_esdorm()==True:
            print ("Este dormitorio tiene", (lista[x].get_camas()), "camas.")


def main():
    lista=[]

    while True:
        respuesta=input("Para introducir los datos de una nueva habitación, introduzca 1 ; Para dar de baja una habitación, introduzca 2 ; Para modificar los datos de una habitación ya existente, introduzca 3 ; Si quiere finalizar el programa, introduzca 4:")
        
        if respuesta=="1":
            datos_hab(lista)

        elif respuesta=="2":
            eliminar_hab(lista)

        elif respuesta=="3":
            modificar_hab(lista)

        elif respuesta=="4":
            fin_programa(lista)
            break ;
        
        else:
            print ("Dato introducido no válido.")

            break ;

if __name__=='__main__':
    main()