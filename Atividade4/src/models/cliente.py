# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

from datetime import datetime
class PedidoCliente:
    def __init__(self, id_cliente, id_pedido):
        self.id_cliente = id_cliente
        self.id_pedido = id_pedido
        self.date = datetime.today().strftime('%d/%m/%Y')