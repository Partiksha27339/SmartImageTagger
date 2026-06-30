import streamlit as st
from openai import OpenAI
from PIL import Image

# Secrets se OpenAI Key lein
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Smart Image Tagger (via ChatGPT)")

uploaded_file = st.file_uploader("Image upload karo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Tag generate karo"):
        # ChatGPT (GPT-4o) ko call karein
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": "Is image ke liye tags suggest karo"}
            ]
        )
        st.write(response.choices[0].message.content)