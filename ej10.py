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


def main():
    lista=[]
    
    respuesta=input("¿Quiere introducir los datos de una nueva habitación?")

    while respuesta.lower()=="si" or respuesta.lower()=="sí":
        largo=input("Introduzca el largo de la habitación:")
        ancho=input("Introduzca el ancho de la habitación:")
        ventanas=input("Introduzca el número de ventanas que tiene la habitación:")
        puertas=input("Introduzca el número de puertas que tiene la habitación:")
        preg=input("¿Desea pintar la habitación?")

        if preg.lower()=="si" or preg.lower()=="sí":
            color=input("Introduzca el color del que quiera pintar la habitación:")
            miHabitacion=Habitacion(largo, ancho, ventanas, puertas)
            miHabitacion.pintar(color)
        else:
            miHabitacion=Habitacion(largo, ancho, ventanas, puertas)

        extra=input("¿La habitación es un dormitorio?")
        if extra.lower()=="si" or extra.lower()=="sí":
            camas=input("Introduzca el número de camas que tiene el dormitorio:")
            miDormitorio=Dormitorio(camas, largo, ancho, ventanas, puertas)
            miDormitorio.set_esdorm(True)
            lista.append(miDormitorio)
        else:
            miHabitacion=Habitacion(largo, ancho, ventanas, puertas)
            lista.append(miHabitacion)
        respuesta=input("¿Quiere introducir los datos de una nueva habitación?")
    
    for x in range (0, len(lista)):
        print(lista[x].get_largo())
        print(lista[x].get_ancho())
        print(lista[x].get_ventanas())
        print(lista[x].get_puertas())
        print(lista[x].get_color())
        if miDormitorio.get_esdorm()==True:
            print(lista[x].get_camas())


if __name__=='__main__':
    main()