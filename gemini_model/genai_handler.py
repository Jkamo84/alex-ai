import google.generativeai as genai
from settings import API_KEY


PLANTILLA = """"
usted es un contador experto en leyes colombianas basadas en la informacion de 2025.
responda a este mensaje 
{mensaje}
pongale un resumen al final de todo lo que se encontró
    """


def call_genai(message):
    genai.configure(api_key=API_KEY)

    # Choose a model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Start a chat session
    chat = model.start_chat(history=[])
    # chat = model.get_chat(id="")

    # Send a message and print the response
    full_message = PLANTILLA.format(message)
    response = chat.send_message(full_message)

    return response.text
