from src.models.user import User
from src.dao.user_dao import UserDAO
from src.controllers.app_controller import App_Controller

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

class UserController():

    # Carrega os dados dos usuários
    def __init__(self) -> None:
        pass

    def checkUser(self,user):
        return user in self.users

    def pegar_user(self, username) -> User:
        user = UserDAO.get_instance().pegar_user(username)
        return user

    def pegar_username(self, username) -> User:
        username = UserDAO.get_instance().pegar_username(username)
        return username

    def checkLogin(self, username, password):
        # Verifica o login do usuário
        try:
            user_teste = User(username=username, password=password, email=None)
            for user in self.users:
                if UserDAO.login_user(user_teste.username, user_teste.password) == True:
                    App_Controller.loginStatus()
                    return True
        except:
            return False

    def registro(self, username, password, email):
        # Registra um novo usuário
        try:
            UserDAO.inserir_usuario(username,password,email)
            return True
        except:
            return False

    def modificacao(self, username, password, email):
        # Altera as informações de um usuário já existente
        try:
            UserDAO.atualizar_usuario(username,password,email)
            return True
        except:
            return False