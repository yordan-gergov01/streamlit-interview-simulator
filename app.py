from openai import OpenAI
import streamlit as st

st.set_page_config(page_title="Streamlit Chat", chat_icon="💬")
st.title("Chatbot")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_mode" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"