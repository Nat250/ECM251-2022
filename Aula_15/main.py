from item import Item
from carrinho import Carrinho

item1 = Item(199, 'Dark Souls', 1)
item2 = Item(350, 'Dark Souls 2', None, 'Continuacao')
item3 = Item(
    preco=350,
    nome='Dark Souls 3',
    descricao='Continuacao')
    # Dessa forma, é apenas necessário escrever os atributos especificados

print(item1 == item2)
print(item2 == item3)
print(item2 == 'Dark Souls 2')