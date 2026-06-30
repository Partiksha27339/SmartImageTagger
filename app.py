import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Key load karo
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# 2. Model setup karo (Gemini 1.5 Flash fast aur free hai)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Smart Image Tagger")

uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Tags Suggest Karo"):
        try:
            # 3. Gemini ko prompt bhejo
            response = model.generate_content(["Is image mein kya dikh raha hai, tags suggest karo", image])
            st.write(response.text)
        except Exception as e:
            st.error(f"Error aaya: {e}")