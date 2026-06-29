import streamlit as st
import os
from dotenv import load_dotenv
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

st.title("AI Image Tagger")
uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    st.write("Processing...")
    # Yahan hum Azure ko connect karenge (3 din baad)