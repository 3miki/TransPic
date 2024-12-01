# TransPic
An AI-powered tool that converts text from images into your desired language. It combines the Gemma Vision model with the Gemma multilingual model to translate text effectively.

## Technology
- PaliGemma: Vision model to identify text from images
- Gemma2(2B): Multilingual model for translation tasks
- Streamlit: Frontend and backend

## Set up
- Set a hugging face token in .env file
- Download [uv](https://docs.astral.sh/uv/getting-started/installation/) (package and dependency manager for python).
- `uv sync` to install dependencies.
- [option] `uv add <package name>` to add new packages

- Run program files To run the python from terminal using PDM and streamlit, use the following command:
`uv run streamlit run dashboard.py`

## To Do
- Add a function to take a picture
- Improve inference speed by using tequniques such as quantization or pruning.
- Improve capabilities of PaliGemma detection into more specific usecases by fine-tuning the PaliGemma on specific datasets such as food, plant or bird names.