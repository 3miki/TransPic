![Cover](/gallery/cover.png)

# TransPic
An AI-powered tool that converts text from images into your desired language. It combines the Gemma Vision model with the Gemma multilingual model to translate text effectively.

## App link: [TransPic](https://transpic.streamlit.app/)

## Technology
- PaliGemma(paligemma-3b-pt-224): Vision model to identify text from images
  - Pre-trained model focuses on object detection
  - 224 pixels for faster inference (but may affect accuracy)
- Gemma2 2B (gemma-2-2b-it): Multilingual model for translation tasks
  - Instruction tuned model for obtaining translations in the desired format
- Streamlit: Frontend and backend framework for building the app interface

## Set Up
- Set a hugging face token(HF_AUTH_TOKEN) in .env file. (modify example.env)
- Download [uv](https://docs.astral.sh/uv/getting-started/installation/) (package and dependency manager for python).
- `uv sync` to install dependencies.
- [option] `uv add <package name>` to add new packages.

- Run program files To run the python from terminal using PDM and streamlit, use the following command: `uv run streamlit run dashboard.py`

## Future Work
- Add a function to take a picture (create a mobile app if feasable).
- Improve inference speed by using tequniques such as quantization or pruning.
- Improve capabilities of PaliGemma detection into more specific usecases by fine-tuning the PaliGemma on specific datasets such as food, plant or bird names.

## App Image
![App image](/gallery/app.png)