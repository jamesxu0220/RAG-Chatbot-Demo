"""Frontend for RAG Chatbot using Streamlit."""

import requests
import streamlit as st

st.title("🧠 RAG Chatbot")

query = st.text_input("Ask something about places to live in NYC Metro Area:")
if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        res = requests.post("http://backend:5000/rag/chat", json={"query": query})
        if res.ok:
            st.success(res.json()["response"])
        else:
            st.error("Something went wrong.")
