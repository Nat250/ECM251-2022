from controllers.user_controller import UserController
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

controller = UserController()
st.title("Bem vindo à loja")
sign_in, sign_up = st.tabs(["Sign In", "Sign Up"])

with sign_in:
    st.write("Para efetuar o log in, insira seu username e password.")
    st.write("Username:")
    username_login = st.text_input(label="Insira o username aqui")
    st.write("Password:")
    pword_login = st.text_input(label="Insira o password aqui",type="password")

    st.button(
        label="Log In",
        help="Clique para entrar.",
        on_click=controller.checkLogin(username_login,pword_login)
    )

with sign_up:
    st.write("Para efetuar o sign up, insira seu email, futuro username e futuro password.")
    st.write("Username:")
    username_signup = st.text_input(key="chave1", label="Insira o username aqui")
    st.write("Password:")
    pword_signup = st.text_input(key="chave2", label="Insira o password aqui",type="password")
    st.write("Email:")
    email_signup = st.text_input(key="chave3", label="Insira o email aqui")

    st.button(
        label="Sign Up",
        help="Clique para se registrar.",
        on_click=controller.registro(username_signup,pword_signup,email_signup)
    )    