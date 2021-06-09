from menu import Menu
from config import session
from sqlalchemy import select
from model.credencial import Credencial
from model.user import User
import getpass

class Controlador:

    user_id = 0
    def __init__(self):
        user = input("Ingrese nombre de usuario: ")
        password = getpass.getpass("Ingrese contraseña: ")
        
        
        if(self.login(user, password)):
            userid = self.get_user_id(user)
            self.start(userid)
        else:
            print("Credenciales incorrectas")

    def start(self, userid):
        menu = Menu(userid)

    def login(self,user,password):

        cred = self.get_credenciales(user,password)

        if(cred):
            return True
        elif(cred == False):
            return False
    
    def get_credenciales(self,user,password):
        try:
            credencial = session.query(Credencial).select_from(Credencial).\
            filter(Credencial.user_name == user, Credencial.password == password).scalar()

            if(credencial.user_name == user and credencial.password == password):
                return True
            

        except Exception as e:
            print('Estoy en excepcion')
            return False


    def get_user_id(self, user):
        uid = session.query(Credencial.user_id).select_from(Credencial).\
        filter(Credencial.user_name == user).scalar()
        self.user_id = uid
        print("UID del usuario", user ,": ", self.user_id)
        return uid