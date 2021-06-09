import config

class Producto(config.Base):
    __tablename__ = 'producto'
    id_producto = config.Column(config.Integer, primary_key=True, nullable = False)
    descripcion = config.Column(config.String(50))
    valor = config.Column(config.Integer)

    def productos_to_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }

    def save(self):
        config.save_to_db(self)

    def listar_productos(self):
        prod = config.select(producto)
        result = config.execute(prod)