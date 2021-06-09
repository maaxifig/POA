import config
import model.orden_canje
import model.producto

class Orden_producto(config.Base):

    __tablename__ = 'orden_producto'
    n_orden = config.Column(config.Integer, config.ForeignKey('orden_canje.n_orden'), primary_key = True, nullable = False)
    #n_orden_producto = config.Column(config.Integer, primary_key = True, nullable = False)
    id_producto = config.Column(config.Integer, config.ForeignKey('producto.id_producto'), primary_key = True, nullable = False)
    cantidad = config.Column(config.Integer)

    model.orden_canje = config.relationship('model.orden_canje.Orden_canje')
    model.producto = config.relationship('model.producto.Producto')


def save(self):
    config.save_to_db(self)