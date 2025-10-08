import numpy as np
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# 1. Data Collection and Preprocessing
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

# Tokenize the text
tokenizer = Tokenizer(num_words=100, oov_token="<unk>")
tokenizer.fit_on_texts(texts + responses)

# Convert text to sequences
input_sequences = tokenizer.texts_to_sequences(texts)
output_sequences = tokenizer.texts_to_sequences(responses)

# Pad sequences to a fixed length
max_sequence_len = max(
    max(len(seq) for seq in input_sequences), max(len(seq) for seq in output_sequences)
)
padded_input_sequences = pad_sequences(
    input_sequences, maxlen=max_sequence_len, padding="post"
)
padded_output_sequences = pad_sequences(
    output_sequences, maxlen=max_sequence_len, padding="post"
)

# Prepare target data for training (one-hot encoded)
vocab_size = len(tokenizer.word_index) + 1
target_data = np.zeros((len(padded_output_sequences), max_sequence_len, vocab_size))
for i, seq in enumerate(padded_output_sequences):
    for t, word_id in enumerate(seq):
        if word_id != 0:  # Ignore padding
            target_data[i, t, word_id] = 1.0

# 2. Model Selection and Architecture
model = Sequential(
    [
        Embedding(vocab_size, 64, input_length=max_sequence_len),
        LSTM(128, return_sequences=True),
        Dense(vocab_size, activation="softmax"),
    ]
)

model.compile(optimizer="adam", loss="categorical_crossentropy")

# 3. Model Training
model.fit(padded_input_sequences, target_data, epochs=50, verbose=0)


# 5. Response Generation
def generate_response(input_text):
    input_seq = tokenizer.texts_to_sequences([input_text])
    padded_input_seq = pad_sequences(input_seq, maxlen=max_sequence_len, padding="post")
    predicted_probs = model.predict(padded_input_seq)[0]

    predicted_words = []
    for timestep in predicted_probs:
        predicted_word_id = np.argmax(timestep)
        if predicted_word_id != 0:
            predicted_word = tokenizer.index_word.get(predicted_word_id)
            if predicted_word:
                predicted_words.append(predicted_word)
    return " ".join(predicted_words)


# Test the model
print(generate_response("hello"))
print(generate_response("how are you"))
print(generate_response("do you know a song?"))
