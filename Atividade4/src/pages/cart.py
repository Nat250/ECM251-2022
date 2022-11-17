from src.controllers.app_controller import App_Controller
from src.controllers.pedido_controller import PedidoController
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

app_Controller = App_Controller()
pedido_Controller = PedidoController()

if 'loginStatusTrue' not in st.session_state:
    st.title("Faça Login primeiro!") 
else:
    st.title("Carrinho")

    st.write("Se quiser comprar mais alguma coisa, vá para a página de produtos.")

    app_Controller.visualizar_pedido

    st.write("Para efetuar sua compra, digite seu cpf:")
    cpf = st.text_input(label="Digite aqui.")

    app_Controller.criar_novo_pedido(cpf)

    st.write("O total do pedido é:")

    app_Controller.fechar_pedido

    st.button(
        label="Pagar",
        help="Clique para pagar por suas compras.",
        on_click=pedido_Controller.deletar_pedido,
        kwargs={"id":pedido_Controller.pegarPedido.id}
        )