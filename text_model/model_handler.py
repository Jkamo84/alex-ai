import os
import numpy as np
import pickle
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


class SimpleChatbot:
    def __init__(
        self,
        model_path="chatbot_model.h5",
        tokenizer_path="tokenizer.pkl",
        max_sequence_len=None,
        texts=None,
        responses=None,
        num_words=100,
        embedding_dim=64,
        lstm_units=128,
    ):
        self.model_path = model_path
        self.tokenizer_path = tokenizer_path
        self.embedding_dim = embedding_dim
        self.lstm_units = lstm_units
        self.num_words = num_words
        self.texts = texts
        self.responses = responses
        self.tokenizer = None
        self.model = None
        self.max_sequence_len = max_sequence_len

        # Try loading pre-trained components
        if os.path.exists(self.model_path) and os.path.exists(self.tokenizer_path):
            self._load()
        elif texts and responses:
            self._prepare_data()
            self.model = self._build_model()
        else:
            raise ValueError(
                "Provide either a trained model/tokenizer or texts/responses for training."
            )

    def _prepare_data(self):
        self.tokenizer = Tokenizer(num_words=self.num_words, oov_token="<unk>")
        self.tokenizer.fit_on_texts(self.texts + self.responses)

        input_sequences = self.tokenizer.texts_to_sequences(self.texts)
        output_sequences = self.tokenizer.texts_to_sequences(self.responses)

        self.max_sequence_len = max(
            max(len(seq) for seq in input_sequences),
            max(len(seq) for seq in output_sequences),
        )

        self.padded_input_sequences = pad_sequences(
            input_sequences, maxlen=self.max_sequence_len, padding="post"
        )
        self.padded_output_sequences = pad_sequences(
            output_sequences, maxlen=self.max_sequence_len, padding="post"
        )

        self.vocab_size = len(self.tokenizer.word_index) + 1

        # One-hot encode targets
        self.target_data = np.zeros(
            (len(self.padded_output_sequences), self.max_sequence_len, self.vocab_size)
        )
        for i, seq in enumerate(self.padded_output_sequences):
            for t, word_id in enumerate(seq):
                if word_id != 0:
                    self.target_data[i, t, word_id] = 1.0

    def _build_model(self):
        model = Sequential(
            [
                Embedding(
                    self.vocab_size,
                    self.embedding_dim,
                    input_length=self.max_sequence_len,
                ),
                LSTM(self.lstm_units, return_sequences=True),
                Dense(self.vocab_size, activation="softmax"),
            ]
        )
        model.compile(optimizer="adam", loss="categorical_crossentropy")
        return model

    def train(self, epochs=50, verbose=0):
        self.model.fit(
            self.padded_input_sequences,
            self.target_data,
            epochs=epochs,
            verbose=verbose,
        )
        self._save()

    def generate_response(self, input_text):
        input_seq = self.tokenizer.texts_to_sequences([input_text])
        padded_input_seq = pad_sequences(
            input_seq, maxlen=self.max_sequence_len, padding="post"
        )
        predicted_probs = self.model.predict(padded_input_seq, verbose=0)[0]

        predicted_words = []
        for timestep in predicted_probs:
            predicted_word_id = np.argmax(timestep)
            if predicted_word_id != 0:
                predicted_word = self.tokenizer.index_word.get(predicted_word_id)
                if predicted_word:
                    predicted_words.append(predicted_word)
        return " ".join(predicted_words)

    def _save(self):
        self.model.save(self.model_path)
        with open(self.tokenizer_path, "wb") as f:
            pickle.dump(
                {
                    "tokenizer": self.tokenizer,
                    "max_sequence_len": self.max_sequence_len,
                    "vocab_size": self.vocab_size,
                },
                f,
            )

    def _load(self):
        self.model = load_model(self.model_path)
        with open(self.tokenizer_path, "rb") as f:
            data = pickle.load(f)
            self.tokenizer = data["tokenizer"]
            self.max_sequence_len = data["max_sequence_len"]
            self.vocab_size = data["vocab_size"]
