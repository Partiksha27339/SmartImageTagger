import streamlit as st
from transformers import pipeline
from PIL import Image

# 1. Hugging Face ka Image Captioning model load karo
@st.cache_resource
def load_model():
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

captioner = load_model()

st.title("Smart Image Tagger (Hugging Face)")

uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
    
    if st.button("Tags/Caption Generate Karo"):
        with st.spinner("Image analyze ho rahi hai..."):
            # Model se result nikalo
            result = captioner(image)
            st.subheader("Result:")
            st.write(result[0]['generated_text'])