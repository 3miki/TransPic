![Cover](/gallery/cover.png)

# TransPic
This app is designed for language learners and travellers who want to identify objects such as food, aminal and plant, and learn their names in their preferred language. 

By translating visual images into text, it makes language acquisition more intuitive and travel experiences more enjoyable!

#### Visit the app [here](https://transpic.streamlit.app/).

## Technology
- PaliGemma(paligemma-3b-pt-224): Vision model to identify text from images
  - Pre-trained model focuses on object detection
  - 224 pixels for faster inference (but may affect accuracy)
- Gemma2 2B (gemma-2-2b-it): Multilingual model for translation tasks
  - Instruction tuned model for obtaining translations in the desired format
- Streamlit: For building the app interface

## Local Setup Instructions
- Add your Hugging Face token (HF_AUTH_TOKEN) to the .env file (use example.env as a reference).
- Download and install [UV](https://docs.astral.sh/uv/getting-started/installation/), a package and dependency manager for Python.
- Run ~~`uv sync`~~ `uv pip install -r pyproject.toml --extra heavy` to install all required dependencies.
- [Optional] To add a new package, use the command: `uv add <package name>`.
- use the following command to execute program using UV and Streamlit: `uv run streamlit run dashboard.py`.

## Challenge
- Deploying two models simultaneously is resource-intensive.
- The PaliGemma can identify only generic categories and cannot distinguish specific species or types.

## Future Work
- Add a feature to capture pictures directly. [added 05-Dec-2024]
- Develop a mobile app if feasable.
- Enhance inference speed and reduce running cost through techniques like quantization or pruning.
- Extend PaliGemma’s detection capabilities to specific use cases by fine-tuning it with specialized datasets, such as food, plant, or bird species.

## Streamlit App link: [TransPic](https://transpic.streamlit.app/)
- Due to resource constraints for running Gemma models, the app currently uses the Gemini API (Gemini flash 1.5 model).
- Language selection: Chinese, Germany, Japanese, Malay, Spanish, Thai (selection is limited for more intuitive interaction).

#### App Image
![App image](/gallery/app2.png)