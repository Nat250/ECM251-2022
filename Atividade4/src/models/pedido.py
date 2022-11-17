# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

class Pedido:
    def __init__(self, id, id_item, quantidade, numero_pedido, id_cliente, data_hora) -> None:
        self._id = id
        self._id_item = id_item
        self._quantidade = quantidade
        self._numero_pedido = numero_pedido
        self._id_cliente = id_cliente
        self._data_hora = data_hora

    def __str__(self) -> str:
        return f'Pedido: id: {self.id} - Item: {self.id_item} - Quantidade: {self.quantidade} - Número do Pedido: {self.numero_pedido} - Cliente: {self.id_cliente} - Data e Hora: {self.data_hora}'