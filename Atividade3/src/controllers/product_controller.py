from models.product import Product

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

class ProductController():
    
    # Carrega os dados dos produtos
    def __init__(self) -> None:
        self.products = [
            Product(name="Koraidon", price="R$ 99,99", url="https://archives.bulbagarden.net/media/upload/thumb/2/24/Koraidon.png/250px-Koraidon.png"),
            Product(name="Cyclizar", price="R$ 39,99", url="https://archives.bulbagarden.net/media/upload/thumb/1/12/Cyclizar.png/250px-Cyclizar.png"),
            Product(name="Miraidon", price="R$ 99,99", url="https://archives.bulbagarden.net/media/upload/thumb/f/fb/Miraidon.png/250px-Miraidon.png")
        ]

    def compra(self,name,price,url):
        # Nao consegui terminar, nao sei o que fazer
        pass