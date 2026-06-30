import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Key Load
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 2. Model Selection (Saaf aur Simple)
# Agar 1.5-flash error de, toh yahan sirf 'gemini-1.5-flash' likhein
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Smart Image Tagger")
uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
    
    if st.button("Tags Suggest Karo"):
        try:
            # Image aur prompt bhejein
            response = model.generate_content(["Is image ke liye tags suggest karo", image])
            st.write(response.text)
        except Exception as e:
            st.error(f"API Error: {e}")
            st.info("Check: Kya aapne AI Studio mein 'Create in new project' kiya hai?")