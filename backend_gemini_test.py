import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_object_name(image: Image, language) -> str:
    generation_config = {
    "temperature": 1.0, # small values for more deterministic output, range from 0.0 to 2.0
    "max_output_tokens": 300, # maximum number of tokens to generate, max 128,000 tokens
    "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )

    # model=genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = f"What is the main item in this image? Respond with only the name of the object in English and provide the translation in {language}."
    response = model.generate_content([prompt, image])
    return response.text

# test the functions
if __name__ == "__main__":

    genai.configure(api_key=os.getenv("API_KEY"))
    image_path = os.path.join(os.path.dirname(__file__), "image/bird.jpg")
    image = Image.open(image_path)
    language = "Chinese"
    response = get_object_name(image, language)
    print("response: ", response)