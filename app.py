import streamlit as st
import requests

st.title("HR Resource Chatbot using LLaMA 3")
query = st.text_input("Ask a resource-related question")

if st.button("Get Recommendation") and query:
    res = requests.post("http://localhost:8000/chat", json={"question": query})
    st.write(res.json()["response"])
