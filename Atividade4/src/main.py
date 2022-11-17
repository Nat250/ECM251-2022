from src.controllers.user_controller import UserController
from src.controllers.app_controller import App_Controller
import streamlit as st

# Nome: Johannes Mattheus Krouwel   RA: 20.01248-9

controller = UserController()
app = App_Controller()

st.title("Bem vindo à loja")
if 'loginStatusTrue' not in st.session_state:
    sign_in, sign_up = st.tabs(["Sign In", "Sign Up"])
else:
    sign_in, sign_up, modify_user = st.tabs(["Sign In", "Sign Up", "Alterar Cadastro"])

with sign_in:
    with st.form(key='Sign in', clear_on_submit=True):
        st.write("Para efetuar o log in, insira seu username e password.")
        st.write("Username:")
        username_login = st.text_input(label="Insira o username aqui")
        st.write("Password:")
        pword_login = st.text_input(label="Insira o password aqui",type="password")

        st.form_submit_button(
            label="Log In",
            help="Clique para entrar.",
            on_click=controller.checkLogin,
            kwargs={"username":username_login,"password":pword_login}
        )

with sign_up:
    with st.form(key='Sign up', clear_on_submit=True):
        st.write("Para efetuar o sign up, insira seu email, futuro username e futuro password.")
        st.write("Username:")
        username_signup = st.text_input(key="chave1", label="Insira o username aqui")
        st.write("Password:")
        pword_signup = st.text_input(key="chave2", label="Insira o password aqui",type="password")
        st.write("Email:")
        email_signup = st.text_input(key="chave3", label="Insira o email aqui")

        st.form_submit_button(
            label="Sign Up",
            help="Clique para se registrar.",
            on_click=controller.registro,
            kwargs={"username":username_signup,"password":pword_signup,"email":email_signup}
        )    

with modify_user:
    with st.form(key='Alterar cadastro', clear_on_submit=True):
        st.write("Para alterar seu cadastro, insira seu novo email, novo username e/ou novo password.")
        st.write("Username:")
        username_signup = st.text_input(key="chave1", label="Insira o username aqui")
        st.write("Password:")
        pword_signup = st.text_input(key="chave2", label="Insira o password aqui",type="password")
        st.write("Email:")
        email_signup = st.text_input(key="chave3", label="Insira o email aqui")

        st.form_submit_button(
            label="Alterar cadastro",
            help="Clique para alterar suas informações.",
            on_click=controller.registro,
            kwargs={"username":username_signup,"password":pword_signup,"email":email_signup}
        )