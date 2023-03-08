# OpenAI Chatbot

This is a simple Flask app that allows users to chat with an OpenAI-powered chatbot. 
Users can input a question, and the chatbot will generate a response based on its training.
The model used is the `text-davinci-002`, and there's a limitation of tokens on the model's response to
1024 tokens.

Please find this app no more than a proof of concept.

Enjoy 😄

## Installation

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Set up your OpenAI API credentials by creating a config.yml file in the config directory with the following format:
    ```yaml
    key: YOUR_API_KEY_HERE
    ```
## Usage
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Navigate to http://localhost:5000 in your web browser.
3. Enter a question or statement in the chat box and press "Send" to receive a response from the chatbot.

# Contributing

This project is open to contributions. If you would like to contribute, please contact "NAME".