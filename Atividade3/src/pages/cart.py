from controllers.app_controller import App_Controller
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

if App_Controller.loginStatus == True:
    st.title("Carrinho")
    # Eu nao faco a menor ideia como fazer isso e provavelmente vou precisar de um gabarito depois
    # Nada que eu fiz funciona 
else:
    st.title("Faça Login primeiro!")