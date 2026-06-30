import streamlit as st
import requests
from PIL import Image
import io

# Hugging Face Public API
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"

st.title("Smart Image Tagger")

uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
    
    if st.button("Tags Generate Karo"):
        with st.spinner("Analyzing..."):
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            
            # API Request
            response = requests.post(API_URL, data=img_byte_arr.getvalue())
            
            if response.status_code == 200:
                result = response.json()
                st.write("Result:", result[0]['generated_text'])
            else:
                st.error("Server busy hai, please wait.")