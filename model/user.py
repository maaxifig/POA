import config


class UsersToDict():
  def users_to_dict(self):
    return { col.name: getattr(self, col.name) for col in self.__table__.columns }


class User(config.Base, UsersToDict):
    __tablename__ = 'user'
    user_id = config.Column(config.Integer, primary_key=True, nullable=False)
    first_name = config.Column(config.String(50))
    last_name = config.Column(config.String(50))
    puntaje = config.Column(config.Integer)


def save(self):
    config.save_to_db(self)