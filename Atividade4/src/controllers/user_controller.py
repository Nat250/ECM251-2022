from models.user import User
from controllers.app_controller import App_Controller

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

class UserController():

    # Carrega os dados dos usuários
    def __init__(self) -> None:
        self.users = [
            User(name="user exemplo", password="pass exemplo", email="exemplo@mail.com"),
        ]

    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, name, password):
        # Verifica o login do usuário
        try:
            user_teste = User(name=name, password=password, email=None)
            for user in self.users:
                if user.name == user_teste.name and user.password == user_teste.password:
                    App_Controller.loginStatus(confirmed=True)
                    return True
            return False
        except TypeError:
            print("Algo deu errado:", TypeError)

    def registro(self, name, password, email):
        # Registra um novo usuário
        try:
            self.users.append(User(name=name, password=password, email=email))
            return True
        except TypeError:
            print("Algo deu errado:", TypeError)