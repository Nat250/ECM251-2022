from controllers.app_controller import App_Controller
from controllers.product_controller import Product_Controller
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

product_Controller = Product_Controller()
if App_Controller.loginStatus == True:
    st.title("Produtos")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://archives.bulbagarden.net/media/upload/thumb/2/24/Koraidon.png/250px-Koraidon.png",
            caption="Koraidon"
        )
        st.button(
        label="Comprar",
        help="Clique para comprar este produto.",
        on_click=product_Controller.compra(name="Koraidon", price="R$ 99,99", url="https://archives.bulbagarden.net/media/upload/thumb/2/24/Koraidon.png/250px-Koraidon.png") # Completar
        )

    with col2:
        st.image(
            "https://archives.bulbagarden.net/media/upload/thumb/1/12/Cyclizar.png/250px-Cyclizar.png",
            caption="Cyclizar"
        )
        st.button(
        label="Comprar",
        help="Clique para comprar este produto.",
        on_click=product_Controller.compra(name="Cyclizar", price="R$ 39,99", url="https://archives.bulbagarden.net/media/upload/thumb/1/12/Cyclizar.png/250px-Cyclizar.png") # Completar
        )

    with col3:
        st.image(
            "https://archives.bulbagarden.net/media/upload/thumb/f/fb/Miraidon.png/250px-Miraidon.png",
            caption="Miraidon"
        )
        st.button(
        label="Comprar",
        help="Clique para comprar este produto.",
        on_click=product_Controller.compra(name="Miraidon", price="R$ 99,99", url="https://archives.bulbagarden.net/media/upload/thumb/f/fb/Miraidon.png/250px-Miraidon.png") # Completar
        )

else:
    st.title("Faça Login primeiro!")