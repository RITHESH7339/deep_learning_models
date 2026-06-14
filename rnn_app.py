import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
model = load_model(
    "models/rnn_imdb.h5"
)
word_index = imdb.get_word_index()
st.title(
    "Movie Review Sentiment Analysis using RNN"
)
review = st.text_area(
    "Enter Movie Review"
)
def encode_review(text):
    words = text.lower().split()
    encoded = []
    for word in words:
        if word in word_index:
            encoded.append(
                word_index[word] + 3
            )
        else:
            encoded.append(2)
    return encoded
if st.button(
    "Predict Sentiment"
):
    encoded_review = encode_review(
        review
    )
    padded_review = pad_sequences(
        [encoded_review],
        maxlen=200
    )
    prediction = model.predict(
        padded_review
    )[0][0]
    if prediction > 0.5:
        st.success(
            "Positive Review"
        )
    else:
        st.error(
            "Negative Review"
        )
    st.info(
        f"Score: {prediction:.2f}"
    )