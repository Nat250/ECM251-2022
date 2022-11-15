from src.controllers.app_controller import App_Controller
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

if 'loginStatusTrue' not in st.session_state:
    st.title("Faça Login primeiro!")
else:
    st.title("Home")
    st.title("Por favor vá a página Produto ou Carrinho para comprar algo.")