![Cover](/gallery/cover.png)

# TransPic
An AI-powered tool that converts text from images into your desired language. It combines the Gemma Vision model with the Gemma multilingual model to translate text effectively.

## Technology
- PaliGemma(paligemma-3b-pt-224): Vision model to identify text from images
  - Pre-trained model focuses on object detection
  - 224 pixels for faster inference (but may affect accuracy)
- Gemma2 2B (gemma-2-2b-it): Multilingual model for translation tasks
  - Instruction tuned model for obtaining translations in the desired format
- Streamlit: Frontend and backend framework for building the app interface

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
- Add a function to capture pictures directly (develop a mobile app if feasable).
- Enhance inference speed and reduce running cost through techniques like quantization or pruning.
- Extend PaliGemma’s detection capabilities to specific use cases by fine-tuning it with specialized datasets, such as food, plant, or bird species.

## Streamlit App link: [TransPic](https://transpic.streamlit.app/)
- Due to resource constraints for running Gemma models, the app currently uses the Gemini API.

#### App Image
![App image](/gallery/app.png)