from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
import streamlit as st
st.set_page_config(page_title="hello")

st.header("world")

molu = input=st.text_input("What you want to covert to speech ?: ",key="input")


submit=st.button("Enter")
if submit:
    print("why are you gay ?")