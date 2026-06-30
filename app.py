import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Key set karo (Streamlit ke secrets se)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# 2. App ka design
st.title("Smart Image Tagger")

uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Tag generate karo"):
        # Gemini model call
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(["Is image ke liye tags suggest karo", image])
        st.write(response.text)