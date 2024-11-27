import pandas as pd
import streamlit as st
import pickle

# Load the model
with open("Model.pkl", "rb") as file:
    model = pickle.load(file)

st.markdown(
    """
    <style>
    body {
        background-color: #E8F5E9; /* Light green background */
        font-family: Arial, sans-serif;
    }
    .stApp {
        background-color: #E8F5E9;
    }
    .title {
        font-size: 40px;
        color: #0B3D0D; /* Very dark green for title */
        font-weight: bold;
        text-align: center;
    }
    .input-label {
        color: #0B3D0D; /* Very dark green for input section label */
        font-size: 24px;
        font-weight: 700;
    }
    .stNumberInput label {
        color: #1B5E20; /* Dark green for input labels */
        font-size: 16px;
        font-weight: 600;
    }
    .stNumberInput input {
        background-color: #ffffff; /* White input background */
        border: 2px solid #66BB6A; /* Light green border */
        border-radius: 8px;
        padding: 10px;
        color: #0B3D0D; /* Darker green text color */
        font-size: 16px;
    }
    .stNumberInput input:focus {
        border-color: #2E7D32; /* Darker green when focused */
        outline: none;
    }
    .stButton button {
        background-color: #1B5E20; /* Dark green button color */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px;
        border: none;
    }
    .stButton button:hover {
        background-color: #0D4D17; /* Even darker green on hover */
    }
    .result-text {
        font-size: 22px;
        color: #0B3D0D; /* Very dark green for result text */
        font-weight: bold;
        text-align: center;
    }
    .info-text, .warning-text {
        color: #0B3D0D; /* Dark green for info and warning messages */
        font-size: 18px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">🌱 Crop Recommendation System</h1>', unsafe_allow_html=True)
st.balloons()

st.markdown('<p class="input-label">Input the required values:</p>', unsafe_allow_html=True)

n = st.number_input("Enter the nitrogen value (N):", min_value=0.0, max_value=100.0, step=0.1)
p = st.number_input("Enter the phosphorus value (P):", min_value=0.0, max_value=100.0, step=0.1)
k = st.number_input("Enter the potassium value (K):", min_value=0.0, max_value=100.0, step=0.1)
temperature = st.number_input("Enter the temperature (°C):", min_value=-10.0, max_value=60.0, step=0.1)
humidity = st.number_input("Enter the humidity (%):", min_value=0.0, max_value=100.0, step=0.1)
ph = st.number_input("Enter the pH value:", min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input("Enter the rainfall (mm):", min_value=0.0, max_value=500.0, step=0.1)

if st.button("SUBMIT", key="submit", help="Click to get the crop recommendation"):
    inputs = [[n, p, k, temperature, humidity, ph, rainfall]]
    input_df = pd.DataFrame(inputs, columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

    prediction = model.predict(input_df)

    st.markdown(f'<p class="result-text">🌱 Recommended crop: <strong>{prediction[0]}</strong></p>', unsafe_allow_html=True)

    if prediction[0] in ["rice", "maize"]:
        st.markdown('<p class="info-text">🌾 Tip: Ensure adequate water availability for optimal growth.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="warning-text">💧 Consider monitoring soil pH and moisture levels regularly for best results.</p>', unsafe_allow_html=True)
