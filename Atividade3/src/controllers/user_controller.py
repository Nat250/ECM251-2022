from models.user import User
from controllers.app_controller import AppController

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

class UserController():

    def __init__(self) -> None:
        # Carrega os dados dos usuários
        self.users = [
            User(name="user exemplo", password="pass exemplo", email="exemplo@mail.com"),
        ]

    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, name, password):
        try:
            user_teste = User(name=name, password=password, email=None)
            for user in self.users:
                if user.name == user_teste.name and user.password == user_teste.password:
                    AppController.loginStatus(confirmed=True)
                    return True
            return False
        except TypeError:
            print("Algo deu errado:", TypeError)

    def registro(self, name, password, email):
        try:
            self.users.append(User(name=name, password=password, email=email))
            return True
        except TypeError:
            print("Algo deu errado:", TypeError)