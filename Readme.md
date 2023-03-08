# OpenAI Chatbot

This is a simple Flask app that allows users to chat with an OpenAI-powered chatbot. 
Users can input a question, and the chatbot will generate a response based on its training.
The model used is the `text-davinci-002`, and there's a limitation of tokens on the model's response to
1024 tokens.

Please find this app no more than a proof of concept.

Enjoy 😄

## Installation
This app is using Flask and is deployed in vercel.com. 
For a local deployment you first need to install the vercel CLI:
 ```bash
    sudo npm i -g vercel
```
## Usage
1. Once vercel is installed, launch the app.
    ```bash
    vercel dev
    ```
2. Navigate to http://localhost:3000 in your web browser.
3. Enter a question or statement in the chat box and press "Send" to receive a response from the chatbot.

# Contributing

This project is open to contributions. If you would like to contribute, please contact "NAME".