from flask import Flask
import config
import sys
from model.user import User
from model.credencial import Credencial
from model.orden_canje import Orden_canje
from model.producto import Producto
from model.orden_producto import Orden_producto

app = Flask(__name__, instance_relative_config=True)

#config
app.config.from_object('config')

# Si para levantar el server le pasamos createdb entonces dropea la BD y la crea de nuevo.
if len(sys.argv) > 1 and 'createdb' == sys.argv[1]:
    config.drop_db()
    config.init_db(True)
else:
    config.init_db(False)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
