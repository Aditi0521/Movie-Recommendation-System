import streamlit as st
import hashlib
from database import create_user, login_user


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')

    if st.button("Register"):
        create_user(new_user, hash_password(new_password))
        st.success("You have successfully created an account!")
        st.info("Go to Login Menu to login")


def login():
    st.subheader("Login Section")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = login_user(username, hash_password(password))
        if user:
            st.session_state.logged_in = True
            st.session_state.user_id = user[0]
            st.success(f"Welcome {username}")
        else:
            st.error("Incorrect username or password")


def logout():
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.success("Logged out successfully")
