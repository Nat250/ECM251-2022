from controllers.app_controller import App_Controller
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

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
        on_click=compra # Completar
        )

    with col2:
        st.image(
            "https://archives.bulbagarden.net/media/upload/thumb/1/12/Cyclizar.png/250px-Cyclizar.png",
            caption="Cyclizar"
        )
        st.button(
        label="Comprar",
        help="Clique para comprar este produto.",
        on_click=compra # Completar
        )

    with col3:
        st.image(
            "https://archives.bulbagarden.net/media/upload/thumb/f/fb/Miraidon.png/250px-Miraidon.png",
            caption="Miraidon"
        )
        st.button(
        label="Comprar",
        help="Clique para comprar este produto.",
        on_click=compra # Completar
        )

else:
    st.title("Faça Login primeiro!")