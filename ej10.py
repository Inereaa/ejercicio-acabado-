class Habitacion():
    def __init__(self, num, largo, ancho, ventanas, puertas):
        self.__num=num
        self.__largo=largo
        self.__ancho=ancho
        self.__ventanas=ventanas
        self.__puertas=puertas
        self.__color="blanco"
        self.__esdorm=False

    def set_num(self, num):
        self.__num=num
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

    def get_num(self):
        return self.__num
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
    def __init__ (self, camas, num, largo, ancho, ventanas, puertas):
        self.__camas=camas
        self.__color="blanco"
        super().__init__(num, largo, ancho, ventanas, puertas)
    def set_camas (self, camas):
        self.__camas=camas
    def get_camas (self):
        return self.__camas
    
    def pintar(self, color):
        self.__color=color
    def get_color(self):
        return self.__color
    


def datos_hab(lista):
        num=input("Introduzca el número de la habitación:")
        largo=input("Introduzca el largo de la habitación (EN METROS):")
        ancho=input("Introduzca el ancho de la habitación (EN METROS):")
        ventanas=input("Introduzca el número de ventanas que tiene la habitación:")
        puertas=input("Introduzca el número de puertas que tiene la habitación:")
        
        global miHabitacion
        miHabitacion=Habitacion(num, largo, ancho, ventanas, puertas)
    
        preg=input("¿Desea pintar la habitación? Introduzca 1 para SÍ, o introduzca 2 para NO:")
        if preg=="1":
            color=input("Introduzca el color del que quiera pintar la habitación:")
            miHabitacion=Habitacion(num, largo, ancho, ventanas, puertas)
            miHabitacion.pintar(color)
        elif preg=="2":
            print ("Ha decidido no pintar la habitación, por lo que se quedará de color blanco.")
        else:
            print ("Dato introducido no válido.")
        
        global extra
        extra=input("¿La habitación tiene dormitorio? Introduzca 1 para SÍ, o introduzca 2 para NO:")
        if extra=="1":
            camas=input("Introduzca el número de camas que tiene el dormitorio:")
            global miDormitorio
            miDormitorio=Dormitorio(camas, num, largo, ancho, ventanas, puertas)
            miDormitorio.set_esdorm(True)
            if preg=="1":
                miDormitorio.pintar(color)
            lista.append(miDormitorio)
        elif extra=="2":
            miHabitacion=Habitacion(num, largo, ancho, ventanas, puertas)
            if preg=="1":
                miHabitacion.pintar(color)
            lista.append(miHabitacion)
        else:
            print ("Dato introducido no válido.")



def eliminar_hab(lista):
    borrar_hab=input("Introduzca el número de la habitación que desea eliminar:")
    if borrar_hab==miHabitacion.get_num():
        lista.remove(miHabitacion)
        print ("Habitación número", (miHabitacion.get_num()), "eliminada con éxito.")
    elif borrar_hab==miDormitorio.get_num():
        lista.remove(miDormitorio)
    else:
        print ("El número de habitación introducida no existe o esta ya ha sido eliminada.")



def modificar_hab(lista):
    nombre_hab=input("Introduzca el número de la habitación que desea modificar:")
    if nombre_hab==miHabitacion.get_num():
        print ("Los datos siguientes son de la habitación número", (miHabitacion.get_num()), ":")
        print ((miHabitacion.get_largo()), "metros de largo")
        print ((miHabitacion.get_ancho()), "metros de ancho")
        print ((miHabitacion.get_ventanas()), "ventanas")
        print ((miHabitacion.get_puertas()), "puertas")
        if extra=="1":
            print ((miDormitorio.get_camas()), "camas")
        elif extra=="2":
            print ("Y no tiene camas, pues no tiene dormitorio.")

        largo=input("Introduzca el nuevo largo de la habitación (EN METROS):")
        miHabitacion.set_largo(largo)
        ancho=input("Introduzca el nuevo ancho de la habitación (EN METROS):")
        miHabitacion.set_ancho(ancho)
        ventanas=input("Introduzca el número de ventanas de la habitación:")
        miHabitacion.set_ventanas(ventanas)
        puertas=input("Introduzca el número de puertas de la habitación:")
        miHabitacion.set_puertas(puertas)
        if extra=="1":
            camas=input("Introduzca el nuevo número de camas del dormitorio:")
            miDormitorio.set_camas(camas)
        elif extra=="2":
            print ("Y no se puede modificar el número de camas, pues no tiene dormitorio.")

    else:
        print("Ha introducido un número de habitación no existente.")



def fin_programa(lista):
    print ("Ha decidido finalizar el programa.")
    for x in range (0, len(lista)):
        print ("Los datos siguientes son de la habitación número", (lista[x].get_num()),":")
        print ("Esta habitación tiene", (lista[x].get_largo()), "metros de largo")
        print ("Esta habitación tiene", (lista[x].get_ancho()), "metros de ancho")
        print ("Esta habitación tiene", (lista[x].get_ventanas()), "ventanas")
        print ("Esta habitación tiene", (lista[x].get_puertas()), "puertas")
        if extra=="2":
            print ("Esta habitación está pintada de color", (lista[x].get_color()))
        if extra=="1":
            print ("Esta habitación está pintada de color", (lista[x].get_color()))
            print ("Además, esta habitación tiene dormitorio, y este tiene", (lista[x].get_camas()), "camas")

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