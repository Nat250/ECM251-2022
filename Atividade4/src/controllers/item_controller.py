from src.models.item import Item
from src.dao.item_dao import ItemDAO

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

class ItemController:
    def __init__(self) -> None:
        pass

    def pegar_item(self, id) -> Item:
        item = ItemDAO.get_instance().pegar_item(id)
        return item

    def pegar_id(self, id) -> Item:
        id = ItemDAO.get_instance().pegar_id(id)
        return id

    def pegar_nome(self, id) -> Item:
        nome = ItemDAO.get_instance().pegar_nome(id)
        return nome

    def pegar_preco(self, id) -> Item:
        preco = ItemDAO.get_instance().pegar_preco(id)
        return preco

    def pegar_link(self, id) -> Item:
        link = ItemDAO.get_instance().pegar_link(id)
        return link

    def inserir_item(self, item) -> bool:
        try:
            ItemDAO.get_instance().inserir_item(item)
        except:
            return False
        return True

    def pegar_todos_itens(self) -> list[Item]:
        itens = ItemDAO.get_instance().get_all()
        return itens