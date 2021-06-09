import config
import model.user

class Orden_canje(config.Base):
    __tablename__ = 'orden_canje'
    n_orden = config.Column(config.Integer, primary_key = True, nullable=False)
    total = config.Column(config.Integer)
    user_id = config.Column(config.Integer, config.ForeignKey('user.user_id'), nullable = False)

    model.user = config.relationship('model.user.User')

def save(self):
    config.save_to_db(self)