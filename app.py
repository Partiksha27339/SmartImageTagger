import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Key Config
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("Secrets mein GOOGLE_API_KEY set nahi hai!")
    st.stop()

# 2. Model Selection Logic (404 Error fix karne ke liye)
def get_model():
    try:
        # Pehle pro try karein, agar na ho toh dusra
        return genai.GenerativeModel('gemini-1.5-pro')
    except Exception:
        return genai.GenerativeModel('gemini-pro')

model = get_model()

# 3. UI
st.title("Smart Image Tagger")
uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Tags Generate Karo"):
        try:
            with st.spinner("Gemini tags generate kar raha hai..."):
                # Gemini ko prompt aur image bhejein
                response = model.generate_content(["Is image mein kya dikh raha hai? Iske liye keywords aur tags suggest karo.", image])
                st.subheader("Tags/Description:")
                st.write(response.text)
        except Exception as e:
            st.error(f"API Error: {e}")
            st.write("Tip: Agar ye error hai, toh shayad aapke project mein 'gemini-1.5-pro' access nahi hai. AI Studio mein naya project banayein.")