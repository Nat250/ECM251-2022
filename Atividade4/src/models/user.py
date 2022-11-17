# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

class User():
    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email
    def __str__(self) -> str:
        return f'User(username:{self.username}, email:{self.email}, password:{self.password})'