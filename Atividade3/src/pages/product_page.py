from controllers.app_controller import AppController
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

if AppController.loginStatus == False:
    st.title("Faça Login primeiro!")