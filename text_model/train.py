from model_handler import SimpleChatbot

texts = [
    "hello",
    "how are you",
    "what is your name",
    "a nice song",
    "Qué son los estados financieros",
]

responses = [
    "hi there",
    "i am fine, thank you",
    "i am a language model",
    "patito patito color de cafe",
    "Los estados financieros son documentos estructurados cuyo objetivo es mostrar la información sobre la situación financiera y el resultado de una persona o empresa. Estos documentos son elaborados por un período determinado, de tal manera que sean útiles para tomar decisiones.",
]

chatbot = SimpleChatbot(texts=texts, responses=responses)
chatbot.train(epochs=50)
