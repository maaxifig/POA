from controladores.ordercontroller import OrderController
from controladores.historycontroller import Historycontroller


class Menu:
    ordercontroller = OrderController()
    historycontroller = Historycontroller()
    def __init__(self,userid):
        self.menu(userid)

    def menu(self, userid):
        print("--------------------MENU---------------------------")
        print('''
            1. Agregar productos al carrito
            2. Mostrar detalles de usuario
            3. Mostrar canjes historicos
            4. Exit
        ''')
        print("---------------------------------------------------")
        
        opcion = int(input("\nIngrese una opcion: "))
        while (opcion < 1 or opcion > 4):
            opcion = int(input("\nIngrese una opcion correcta: "))
        if opcion == 1:
            self.ordercontroller.listar_productos(userid)
            self.menu(userid)
        elif opcion == 2:
            self.historycontroller.detalle_usuario(userid)
            self.menu(userid)
        elif opcion == 3:
            
            self.historycontroller.listar_ordenes(userid)
            menu_salir = input("Desea volver al menu o salir? m/s: ")
            while(menu_salir != 's' and menu_salir != 'm'):
                menu_salir = input("Ingrese opcion correcta. Desea volver al menu o salir? m/s: ")
            if(menu_salir == 'm'):
                self.menu(userid)
            elif(menu_salir == 's'):
                exit

        elif opcion == 4:
            print("Salir")





  






            
