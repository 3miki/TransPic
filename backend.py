import os
from PIL import Image
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import AutoProcessor, PaliGemmaForConditionalGeneration, pipeline

load_dotenv()

token=os.getenv("HF_AUTH_TOKEN")
login(token)
os.environ["TOKENIZERS_PARALLELISM"] = "false"


def get_object_name(image: Image) -> str:
    model_id = "google/paligemma-3b-mix-224"
    model = PaliGemmaForConditionalGeneration.from_pretrained(model_id)
    processor = AutoProcessor.from_pretrained(model_id)

    prompt = "<image><bos> What is in the image? Describe the main item in the image."
    inputs = processor(image, prompt, return_tensors="pt")

    raw_output = model.generate(**inputs, max_new_tokens=50)

    decode_output = processor.batch_decode(raw_output, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return decode_output

# vision_model_id = "google/paligemma-3b-mix-224"
# vision_model = PaliGemmaForConditionalGeneration.from_pretrained(vision_model_id)
# processor = AutoProcessor.from_pretrained(vision_model_id)
# prompt = "<image><bos> What is in the image? describe the main item in the image in Japanese."
# image_file = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg?download=true"
# raw_image = Image.open(requests.get(image_file, stream=True).raw)
# inputs = processor(raw_image, prompt, return_tensors="pt")
# raw_output = vision_model.generate(**inputs, max_new_tokens=20)
# decode_output = processor.batch_decode(raw_output, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]


def translate_object_name(object_name: str, language: str) -> str:
    model_id = "google/gemma-2-2b-it"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        device="mps",  # to run on a Mac device
        max_new_tokens=50, 
        repetition_penalty=1.2,  # higher than 1.0 is less likely to repeat text
        no_repeat_ngram_size=2, # prevent repeating 2-word sequences
    )

    input_text = f"Translate the following word into {language}. Answer only the translation and do not include this input message. The word is: " + object_name
    outputs = pipe(input_text)
    response = outputs[0]["generated_text"]
    return response


# pipe = pipeline(
#     "text-generation",
#     model="google/gemma-2-2b-it",
#     device="mps",  # "mps" to run on a Mac device
#     max_new_tokens=50, 
#     repetition_penalty=1.2,  # higher than 1.0 is less likely to repeat text
#     no_repeat_ngram_size=2, # prevent repeating 2-word sequences
# )

# decode_output = 'flower' # example
# input_text = "Translate the following word into Japanese. Answer only the translation and do not include this input message. The word is: " + decode_output
# outputs = pipe(input_text, max_new_tokens=256)
# response = outputs[0]["generated_text"]
# print("input: ", input_text)
# print("response: ", response)


# test the functions
if __name__ == "__main__":
    image_path = os.path.join(os.path.dirname(__file__), "image/bird.jpg")
    image = Image.open(image_path)
    language = "Japanese"

    object_name = get_object_name(image)
    print("Original word:", object_name)
    
    translation = translate_object_name(object_name, language)
    print("Translation:", translation)