# TransPic
AI-powered tool that converts text from images into your desired language. It combines OCR technology with translation models to learn new language effectively.

## TO DO
Frontend
- create file upload(image) and language selection [done]
- display translation [ok]
- improve design
- add input text field for hugging face auth token from user (user need to do "Request Access" for gemma models)

Backend
- use Pali gemma to identify objects from images [do prompt engineer]
- use Gemma 2 to translate the object name [need to prompt engineer/fine-tune]


## Set up
- Hugging face token
- Download [uv](https://docs.astral.sh/uv/getting-started/installation/) (package and dependency manager for python).
- `uv sync` to install dependencies.
- [option] `uv add <package name>` to add new packages

- Run program files To run the python from terminal using PDM and streamlit, use the following command:

`uv run streamlit run dashboard.py`