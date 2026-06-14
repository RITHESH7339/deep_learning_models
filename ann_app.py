import streamlit as st
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

st.set_page_config(
    page_title="ANN Classifier",
    page_icon="🤖",
    layout="wide"
)

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

st.title("🤖 ANN Classification App")

@st.cache_resource
def train_model():

    # Load dataset
    data = load_breast_cancer()

    X = data.data
    y = data.target

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # ANN Model
    model = Sequential([
        Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(16, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    model.fit(
        X_train,
        y_train,
        epochs=20,
        batch_size=32,
        verbose=0
    )

    accuracy = model.evaluate(X_test, y_test, verbose=0)[1]

    return model, scaler, data, accuracy


with st.spinner("Training ANN..."):
    model, scaler, data, accuracy = train_model()

st.success(f"Model Trained Successfully! Accuracy: {accuracy:.2%}")

st.header("Enter Feature Values")

inputs = []

for feature in data.feature_names:
    value = st.number_input(
        feature,
        value=float(np.mean(data.data[:, list(data.feature_names).index(feature)]))
    )
    inputs.append(value)

if st.button("Predict"):

    sample = np.array(inputs).reshape(1, -1)

    sample_scaled = scaler.transform(sample)

    prediction = model.predict(sample_scaled, verbose=0)

    probability = prediction[0][0]

    st.subheader(f"Probability: {probability:.4f}")

    if probability >= 0.5:
        st.success("Prediction: Benign")
    else:
        st.error("Prediction: Malignant")
