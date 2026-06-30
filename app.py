import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuration
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 2. Dynamic Model Detection (404 Error fix karne ke liye)
def get_available_model():
    # Yeh list check karega ki aapke project mein kya available hai
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            # Hum 'gemini-1.5' ya 'gemini-pro' dhund rahe hain
            if 'gemini-1.5' in m.name or 'gemini-pro' in m.name:
                return genai.GenerativeModel(m.name)
    return None

model = get_available_model()

st.title("Smart Image Tagger")

if model is None:
    st.error("Error: Aapke project mein koi bhi Gemini model available nahi hai. AI Studio mein NAYA PROJECT banayein.")
else:
    uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")
        
        if st.button("Tags Suggest Karo"):
            try:
                response = model.generate_content(["Is image ke liye tags suggest karo", image])
                st.write(response.text)
            except Exception as e:
                st.error(f"Execution Error: {e}")