class Habitacion():
    def __init__(self, largo, ancho, ventanas, puertas):
        self.__largo=largo
        self.__ancho=ancho
        self.__ventanas=ventanas
        self.__puertas=puertas

    def set_largo(self, largo):
        self.__largo=largo
    def set_ancho(self, ancho):
        self.__ancho=ancho
    def set_ventanas(self, ventanas):
        self.__ventanas=ventanas
    def set_puertas(self, puertas):
        self.__puertas=puertas

    def get_largo(self):
        return self.__largo
    def get_ancho(self):
        return self.__ancho
    def get_ventanas(self):
        return self.__ventanas
    def get_puertas(self):
        return self.__puertas

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
        extra=input("¿La habitación es un dormitorio?")
        if extra.lower()=="si" or extra.lower()=="sí":
            camas=input("Introduzca el número de camas que tiene el dormitorio:")
            miDormitorio=Dormitorio(camas, largo, ancho, ventanas, puertas)
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
        print(lista[x].get_camas())

if __name__=='__main__':
    main()
    

