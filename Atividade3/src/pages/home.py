from controllers.app_controller import App_Controller
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

if App_Controller.loginStatus == True:
    st.title("Home")
else:
    st.title("Faça Login primeiro!")