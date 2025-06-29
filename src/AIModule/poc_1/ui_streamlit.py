import sys
import os
# Add project root (one level above src) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.AIModule.poc_1.bedrock_client import call_claude
import streamlit as st

st.title("📊 Investor Education Chatbot")
st.markdown("Ask any investment-related question below:")

question = st.text_input("Your Question")

if question:
    with st.spinner("Thinking..."):
        response = call_claude(question)
        st.success(response)

