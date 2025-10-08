import google.generativeai as genai
from settings import API_KEY


def call_genai(message):
    genai.configure(api_key=API_KEY)

    # Choose a model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Start a chat session
    chat = model.start_chat(history=[])

    # Send a message and print the response
    response = chat.send_message(message)

    return response.text
