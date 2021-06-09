import config
import model.user

class Credencial(config.Base):
    __tablename__ ='credencial'
    user_name = config.Column(config.String(50), primary_key=True, nullable = False)
    password = config.Column(config.String(50))
    user_id = config.Column(config.Integer, config.ForeignKey('user.user_id'), nullable = False)

    model.user = config.relationship('model.user.User')

def save(self):
    config.save_to_db(self)

def credencial_to_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }