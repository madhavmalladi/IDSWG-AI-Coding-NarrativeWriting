import streamlit as st
from striprtf.striprtf import rtf_to_text
import pandas as pd
import numpy as np

st.title("AI Patient Summarizer")

uploaded_file = st.file_uploader("Please Upload the Patient Data (RTF)", type = "rtf")
if uploaded_file:
    content = uploaded_file.getvalue().decode("utf-8")
    # Convert the rtf file into normal text
    text = rtf_to_text(content)
