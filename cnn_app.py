import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Dark theme with cyan accents
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
    color: #e0e6ed;
}

h1, h2, h3 {
    color: #00d9ff !important;
    text-shadow: 0 0 10px rgba(0, 217, 255, 0.3);
}

.stButton > button {
    background: linear-gradient(135deg, #00d9ff 0%, #0099cc 100%) !important;
    color: #0a0e27 !important;
    border: none !important;
    font-weight: bold !important;
}

.stButton > button:hover {
    box-shadow: 0 0 15px rgba(0, 217, 255, 0.5) !important;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="CNN - Handwritten Digit Recognition",
    page_icon="🎨",
    layout="wide"
)

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
