import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from tensorflow.keras.models import load_model

# Function to load models
@st.cache_resource
def load_models():
    lstm_model = load_model('/content/drive/MyDrive/spam_models/lstm_model.h5')  # Update the path if necessary
    with open('/content/drive/MyDrive/spam_models/svm_model.pkl', 'rb') as svm_file:
        svm_classifier = pickle.load(svm_file)
    with open('/content/drive/MyDrive/spam_models/scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return lstm_model, svm_classifier, scaler

# Load the models and scaler
lstm_model, svm_classifier, scaler = load_models()

# Title of the app
st.title("Spam Classification Application")

# User input for spam features (adjust the feature names based on your dataset)
st.write("Enter the email features for prediction:")

# Modify these inputs based on your dataset
crl_tot = st.number_input("Crl.Tot", min_value=0.0, format="%.2f")
dollar = st.number_input("Dollar", min_value=0.0, format="%.2f")
bang = st.number_input("Bang", min_value=0.0, format="%.2f")
money = st.number_input("Money", min_value=0.0, format="%.2f")
n000 = st.number_input("N000", min_value=0.0, format="%.2f")
make = st.number_input("Make", min_value=0.0, format="%.2f")
receive = st.number_input("Receive", min_value=0.0, format="%.2f")

# Combine input into an array
input_data = np.array([[crl_tot, dollar, bang, money, n000, make, receive]])

# Prediction button
if st.button("Predict"):
    # Scale input using the trained scaler
    input_scaled = scaler.transform(input_data)

    # Reshape input for LSTM model (samples, timesteps, features)
    input_lstm = input_scaled.reshape((input_scaled.shape[0], 1, input_scaled.shape[1]))

    # Extract features using the LSTM model
    lstm_features = lstm_model.predict(input_lstm)

    # Predict using the SVM model
    prediction = svm_classifier.predict(lstm_features)

    # Display the prediction result
    if prediction[0] == 1:
        st.write("Prediction: The email is **Spam**")
    else:
        st.write("Prediction: The email is **Not Spam**")
