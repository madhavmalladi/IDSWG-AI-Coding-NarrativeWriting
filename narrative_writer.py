import streamlit as st
from striprtf.striprtf import rtf_to_text
import requests
import pandas as pd
import numpy as np

st.title("AI Patient Summarizer")

uploaded_file = st.file_uploader("Please Upload the Patient Data (RTF)", type = "rtf")
if uploaded_file:
    content = uploaded_file.getvalue().decode("utf-8")
    # Convert the rtf file into normal text
    text = rtf_to_text(content)
    input = st.text_area("Input to model:", value = text, height = 300)

    # Running the model
    if st.button("Run Llama Summary"):
        with st.spinner("Summarizing"):
            response = requests.post("http://localhost:11434/api/generate", json = {"model": "llama2", "prompt": input, "stream": False})
            result = response.json()
            st.text_area("Llama output:", result, height = 300)