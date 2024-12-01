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

st.info("By using this app, you accept the Google Gemma's Terms of Use found at:\nai.google.dev/gemma/terms")

hf_auth_token = token=os.getenv("HF_AUTH_TOKEN")
login(hf_auth_token)
# st.text_input("Enter your Hugging Face API token(Token will be cleared every session so please keep the copy in safe place.)", type="password")
# if st.button("Submit", key="submit_button"):
    # login(hf_auth_token)
    # st.success("Successfully logged in to Hugging Face")

# upload image file
# st.write("Upload a image here:")
uploaded_file = st.file_uploader("Choose an image file 🖼️", type=["jpg", "jpeg", "png"])

# st.write("Select a language to translate:")
language = st.selectbox("Select a language 💬", ["Japanese", "Chinese", "Spanish"])

# check if image file has been uploaded
if uploaded_file:
    image = Image.open(uploaded_file)
    # display the image
    st.image(image, caption="Uploaded Image", width=300)

    if st.button("Translate", key="translate_button"):    
        with st.spinner('Translating image...'):
            # call models to generate the answer
            image_name = get_object_name(image)
            st.write("Identified object name is: ", image_name)

            translation = translate_object_name(image_name, language)
            st.write("The translation is: ", translation)