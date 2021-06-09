from model.producto import Producto
from model.orden_canje import Orden_canje, save
from model.orden_producto import Orden_producto, save
from model.user import User
from config import session
from sqlalchemy import select, func, update
from collections import Counter
import statistics

class OrderController:

    productList = []
    cargar_lista_primera_vez = 0
    def listar_productos(self, userid):
        products = session.query(Producto)
        
        if (self.cargar_lista_primera_vez == 0):
            for product in products:    
                self.productList.append(product.productos_to_dict())
            self.cargar_lista_primera_vez = self.cargar_lista_primera_vez + 1
        for i in range (0, len(self.productList)):
            print(str(self.productList[i].get('id_producto')),':', self.productList[i].get('descripcion'), ' -- Valor: '+ str(self.productList[i].get('valor')))
        
        self.agregar_producto(self.productList, userid)
        

    def agregar_producto(self, lista, userid):
       
        total = 0
        otro_producto = 's'
        orden_canje_list = []
        puntaje = session.query(User.puntaje).select_from(User).\
            filter(User.user_id == userid).scalar()

        print(f"Usted dispone de {puntaje} puntos\n")


        while(otro_producto == 's'):
            id_producto_seleccionado = int(input("\nIngrese numero de producto para canjear: "))
            while(id_producto_seleccionado < 1 or id_producto_seleccionado > len(lista)):
                id_producto_seleccionado = int(input("\nIngrese numero de producto valido: "))

            producto = session.query(Producto).select_from(Producto).\
                filter(Producto.id_producto==id_producto_seleccionado).scalar()

            p_restantes = puntaje - total

            if(total <= puntaje and producto.valor <= p_restantes):
                
                total = total + producto.valor
                print("Total de puntos a canjear hasta ahora: ", total)
                prod_seleccionado = lista[id_producto_seleccionado - 1].get('descripcion')
                print(prod_seleccionado)
                orden_canje_list.append(producto)
            else:
                print("No le alcanzan los puntos. Seleccione otro producto.")

            otro_producto = input("\nDesea canjear otro producto? s/n: ")
            while(otro_producto!='s' and otro_producto!='n'):
                otro_producto = input("Ingrese opcion correcta. Desea canjear otro producto? s/n: ")

        print("----------------------------------------")
        print("Termino de elegir, sus productos son:")

        for productos in orden_canje_list:
           print(productos.descripcion)
        print("Por un total de: ", total)
        print("----------------------------------------")

        canjea = input("\nDesea confirmar su orden ahora o quiere editarla? c/e: ")
        while(canjea != 'c' and canjea != 'e'):
            canjea = input("Ingrese opcion correcta. Confirmar o editar? c/e: ")

        if(canjea == 'c'):
            orden_canje = Orden_canje()
            orden_canje.user_id = userid
            orden_canje.total = total
            save(orden_canje)

            sobra_puntos = puntaje - total
            self.actualizar_puntos(sobra_puntos, userid)

            self.generar_orden_producto(orden_canje_list)

        elif(canjea == 'e'):
            self.agregar_producto(self.productList,userid)
        

    def generar_orden_producto(self,lista_productos):

        max_orden = session.query(func.max(Orden_canje.n_orden)).scalar()
        print("-------------------------------------------")
        print("Numero de orden: ",max_orden)

        self.ordenar(lista_productos)

        for i in range(0,len(lista_productos)):
            if(i!=0):
                
                if (lista_productos[i].id_producto != lista_productos[i - 1].id_producto):
                    self.calcular_cantidad_productos(lista_productos, max_orden,i)

            else:
                self.calcular_cantidad_productos(lista_productos, max_orden,i)

    def actualizar_puntos(self, puntos, userid):
        stmt = (
        update(User).
        where(User.user_id == userid).
        values(puntaje = puntos)
        )
        session.execute(stmt)
        session.commit()

    def ordenar(self, lista):
        for num_pasada in range(len(lista)-1,0,-1):
            for i in range(num_pasada):
                if lista[i].id_producto>lista[i+1].id_producto:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux

    def calcular_cantidad_productos(self, lista_productos, max_orden, i):
        lista_cantidad = list(filter(lambda p: p.id_producto == lista_productos[i].id_producto, lista_productos))
        cant = len(lista_cantidad)
        print('Producto: ', lista_cantidad[0].descripcion, " Cantidad: ", cant)
        
        orden_producto = Orden_producto()
        orden_producto.n_orden = max_orden
        orden_producto.id_producto = lista_cantidad[0].id_producto
        orden_producto.cantidad = cant
        save(orden_producto)


