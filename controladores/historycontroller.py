from model.user import User
from model.orden_canje import Orden_canje, save
from model.orden_producto import Orden_producto, save
from model.producto import Producto
from config import session
from sqlalchemy import select, func

class Historycontroller:

    def listar_ordenes(self,userid):
        results =  session.query(Orden_producto.n_orden, Orden_producto.id_producto, Producto.descripcion, Orden_producto.cantidad). \
            select_from(Orden_canje).join(Orden_producto).join(Producto). \
            filter(Orden_producto.n_orden == Orden_canje.n_orden and Orden_producto.id_producto == Producto.id_producto).\
            where(Orden_canje.user_id == userid).\
            order_by(Orden_producto.n_orden).all()

        print("----------------Results--------------------")
        print("Numero orden - ID Producto - Descripcion - Cantidad")
        for i in range (0,len(results)):
            print(results[i].n_orden,"\t\t",results[i].id_producto,"\t\t", results[i].descripcion,"\t\t", results[i].cantidad)
        print("----------------Results--------------------")

    def detalle_usuario(self, userid):
        detalles = session.query(User).select_from(User).\
            where(User.user_id == userid).scalar()

        print("\n----------------Detalles de usuario--------------------")
        print('ID: ', detalles.user_id)
        print('Nombre: ', detalles.first_name, detalles.last_name)
        print('Puntos disponibles: ',detalles.puntaje)
        print("-------------------------------------------------------")
        