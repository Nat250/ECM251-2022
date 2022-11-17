from src.controllers.app_controller import App_Controller
from src.controllers.product_controller import Product_Controller
from src.controllers.pedido_controller import PedidoController
from src.controllers.item_controller import ItemController
from src.controllers.user_controller import UserController
from src.models.cliente import PedidoCliente
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

app_Controller = App_Controller()
product_Controller = Product_Controller()
pedido_Controller = PedidoController()
item_Controller = ItemController()
user_Controller = UserController()
pedido_Cliente = PedidoCliente()

if 'loginStatusTrue' not in st.session_state:
    st.title("Faça Login primeiro!")

else:

    st.title("Produtos")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            item_Controller.pegar_link("1"),
            caption=item_Controller.pegar_nome("1")
        )
        quantidade_1 = st.text_input(label="Insira quantos você quer comprar aqui.")
        st.button(
        label="Comprar",
        help="Clique para comprar este produto.",
        on_click=app_Controller.adicionar_item_no_pedido,
        kwargs={"id_item":item_Controller.pegar_id("1"), "quantidade":quantidade_1}
        )

    with col2:
        st.image(
            item_Controller.pegar_link("2"),
            caption=item_Controller.pegar_nome("2")
        )
        quantidade_2 = st.text_input(label="Insira quantos você quer comprar aqui.")
        st.button(
        label="Comprar",
        help="Clique para comprar este produto.",
        on_click=app_Controller.adicionar_item_no_pedido,
        kwargs={"id_item":item_Controller.pegar_id("2"), "quantidade":quantidade_2}
        )

    with col3:
        st.image(
            item_Controller.pegar_link("3"),
            caption=item_Controller.pegar_nome("3")
        )
        quantidade_3 = st.text_input(label="Insira quantos você quer comprar aqui.")
        st.button(
        label="Comprar",
        help="Clique para comprar este produto.",
        on_click=app_Controller.adicionar_item_no_pedido,
        kwargs={"id_item":item_Controller.pegar_id("3"), "quantidade":quantidade_3}
        )