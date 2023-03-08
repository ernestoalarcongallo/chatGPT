import os
from flask import Flask, render_template, request

from src.facades.davinci import authenticate, generate_response

app = Flask(__name__)

# Set up OpenAI API credentials
authenticate(os.environ.get('OPENAI_KEY'))

# Initialize list of chat messages with initial prompt
messages = [{'text': 'Please ask a question', 'is_user': False}]


@app.route('/')
def home():
    return render_template('chat.html', messages=messages)


@app.route("/", methods=["POST"])
def chat():
    user_message = request.form['question']
    bot_response = generate_response(user_message)

    messages.append({'text': user_message, 'is_user': True})
    messages.append({'text': bot_response, 'is_user': False})

    return render_template("chat.html", messages=messages)
