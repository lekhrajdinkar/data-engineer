import streamlit as st
from src.AIModule.poc_1.bedrock_client import call_claude

st.title("📊 Investor Education Chatbot")
st.markdown("Ask any investment-related question below:")

question = st.text_input("Your Question")

if question:
    with st.spinner("Thinking..."):
        response = call_claude(question)
        st.success(response)

