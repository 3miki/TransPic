import os
from PIL import Image
import warnings
import streamlit as st
from dotenv import load_dotenv
# from backend import get_object_name, translate_object_name

load_dotenv()
warnings.filterwarnings("ignore", category=DeprecationWarning, message="The `use_column_width` parameter has been deprecated")

st.title('TransPic 📷')

# upload image file
st.write("Upload a image here:")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

st.write("Select a language to translate:")
language = st.selectbox("Select a language", ["Japanese", "Chinese", "Spanish"])

# check if image file has been uploaded
if uploaded_file:
    image = Image.open(uploaded_file)
    # display the image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Translate", key="translate_button"):    
        with st.spinner('Translating image...'):
            # call models to generate the answer
            st.write("To do: call the backend functions here")
            # image_name = get_object_name(image)
            # st.write("Original word:", image_name)

            # translation = translate_object_name(image_name, language)
            # st.write("Translation is:", translation)