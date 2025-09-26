import google.generativeai as genai

API_KEY = "YOUR_API_KEY"
genai.configure(api_key=API_KEY)

# Choose a model
model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session
chat = model.start_chat(history=[])

# Send a message and print the response
response = chat.send_message("What is your purpose?")
print(response.text)
