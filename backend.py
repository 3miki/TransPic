import os
from PIL import Image
from dotenv import load_dotenv
from transformers import AutoProcessor, PaliGemmaForConditionalGeneration, pipeline

load_dotenv()

def get_object_name(image: Image) -> str:
    model_id = "google/paligemma-3b-pt-224"
    model = PaliGemmaForConditionalGeneration.from_pretrained(model_id)
    processor = AutoProcessor.from_pretrained(model_id)

    prompt = "What is the main item in this image?"
    inputs = processor(image, prompt, return_tensors="pt")

    raw_output = model.generate(
        **inputs,
        max_new_tokens=20,
        repetition_penalty=1.2,
    )

    try:
        decoded_output = processor.decode(raw_output[0], skip_special_tokens=True)[len(prompt):].strip()
        print("decode_output: ", decoded_output)
    except Exception as e:
        print("Error: ", e)

    return decoded_output


def translate_object_name(object_name: str, language: str) -> str:
    model_id = "google/gemma-2-2b-it"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        device="mps",  # to run on a Mac device
        max_new_tokens=20, 
        repetition_penalty=1.2,  # higher than 1.0 is less likely to repeat text
        no_repeat_ngram_size=2, # prevent repeating 2-word sequences
    )

    input_text = f"What is the following word in {language}. Respond with only the {language} translation excluding description, any special charactors. " + object_name

    outputs = pipe(input_text)

    try:
        response = outputs[0]["generated_text"][len(input_text):].strip()
        print("unprocessed response: ",outputs[0]["generated_text"])
        print("response: ", response)
    except Exception as e:
        print("Error: ", e)
    return response


# test the functions
if __name__ == "__main__":
    image_path = os.path.join(os.path.dirname(__file__), "image/bird.jpg")
    image = Image.open(image_path)
    language = "Japanese"

    object_name = get_object_name(image)
    print("Original word:", object_name)

    # object_name = "flower"
    translation = translate_object_name(object_name, language)
    print("Translation:", translation)