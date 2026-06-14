import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("models/cnn_mnist.h5")

st.title("Handwritten Digit Recognition using CNN")

uploaded_file = st.file_uploader(
    "Upload Digit Image",
    type=["png","jpg","jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        width=200
    )

    image = image.convert("L")

    image = image.resize((28,28))

    img_array = np.array(image)

    img_array = img_array / 255.0

    img_array = img_array.reshape(
        1,
        28,
        28,
        1
    )

    prediction = model.predict(
        img_array
    )

    digit = np.argmax(
        prediction
    )

    confidence = np.max(
        prediction
    )

    st.success(
        f"Predicted Digit: {digit}"
    )

    st.info(
        f"Confidence: {confidence:.2f}"
    )