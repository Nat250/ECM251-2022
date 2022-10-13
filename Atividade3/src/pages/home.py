from controllers.app_controller import App_Controller
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

if App_Controller.loginStatus == True:
    st.title("Home")
    st.title("Por favor vá a página Produto ou Carrinho para comprar algo.")
else:
    st.title("Faça Login primeiro!")