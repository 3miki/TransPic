import os
from PIL import Image
import warnings
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import login
from backend import get_object_name, translate_object_name

load_dotenv()
warnings.filterwarnings("ignore", category=DeprecationWarning, message="The `use_column_width` parameter has been deprecated")

st.title('TransPic 📷')

# display disclaimer
st.info("By using this app, you accept the Google Gemma's Terms of Use found at:\nai.google.dev/gemma/terms")

# login to Hugging Face
hf_auth_token = token=os.getenv("HF_AUTH_TOKEN")
login(hf_auth_token)

# upload image file
uploaded_file = st.file_uploader("Choose an image file 🖼️", type=["jpg", "jpeg", "png"])

# select language
language = st.selectbox("Select a language 💬", ["Japanese", "Chinese", "Spanish"])

# show button when image is uploaded
if uploaded_file:
    # display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    if st.button("Translate", key="translate_button"):    
        with st.spinner('Translating image...'):
            # run models to generate answers
            image_name = get_object_name(image)
            st.write("Identified object name is: ", image_name)

            translation = translate_object_name(image_name, language)
            st.write("The translation is: ", translation)