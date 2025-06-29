import streamlit as st
from src.AIModule.poc_1.bedrock_client import call_claude

st.title("📊 Investor Education Chatbot")
question = st.text_input("Ask your question:")
if question:
    answer = call_claude(question)
    st.write(answer)
