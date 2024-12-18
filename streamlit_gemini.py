import os
from PIL import Image
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
st.title('TransPic 📷')

st.write("Upload an image of the object you want to identify and choose your language for translation.")

# set up API key
st.info("This app uses the Gemini-Flash 1.5 model for its responses. To use it, you’ll need a Google Gemini API key. Get your key [here](https://ai.google.dev/gemini-api/docs/api-key).")
api_key_input = st.text_input("Step 1: Enter your Gemini API Key 🗝️", type="password")

# select language
language = st.selectbox("Step 2: Select a language 💬", ["Chinese", "Germany", "Japanese", "Malay", "Spanish", "Thai"])

# upload image file
uploaded_file = st.file_uploader("Step 3: Choose an image file or take a picture 🖼️", type=["jpg", "jpeg", "png"])

# camera mode
enable_camera = st.checkbox("Enable camera 📷")
captured_image = st.camera_input("Take a picture", disabled=not enable_camera)

image_path = None
if uploaded_file:
    image_path = uploaded_file

if captured_image:
    image_path = captured_image

# display image and traslate button when image is uploaded
if image_path:
    image = Image.open(image_path)
    st.image(image, caption="Uploaded Image", width=300)
    # action when button is clicked
    if st.button("Translate", key="translate_button"):
        if not api_key_input:
            st.error("Please enter your Gemini API Key.")
        elif not language:
            st.error("Please select a language.")
        else:
            with st.spinner('Translating image...'):
                # run models to generate answers
                genai.configure(api_key=api_key_input)
                generation_config = {
                "temperature": 0.8, # range from 0.0 to 2.0(creative)
                "max_output_tokens": 300, # max 128,000 tokens
                "response_mime_type": "text/plain",
                }
                model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=generation_config,
                )
                
                prompt = f"What is the main item in this image? Respond with only the name of the object in English and provide the translation in {language}. Format your response as follows: 'object_name, translation'."
                response = model.generate_content([prompt, image])
                print(response.text)
                # display response
                st.write("Identified object name is: ")
                st.subheader(response.text)