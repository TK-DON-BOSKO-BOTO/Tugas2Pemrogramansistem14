import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# Muat model
model = tf.keras.models.load_model('spam_classifier_model.h5', custom_objects={'custom_object_name': custom_object})

# Inisialisasi scaler
scaler = StandardScaler()

# Fungsi untuk membuat prediksi
def predict_spam(features):
    features_scaled = scaler.transform(features)
    features_scaled = np.reshape(features_scaled, (features_scaled.shape[0], 1, features_scaled.shape[1]))
    prediction = model.predict(features_scaled)
    return (prediction > 0.5).astype("int32")

# Antarmuka pengguna
st.title("Spam Classifier")
st.write("Masukkan fitur email yang akan dianalisis:")

# Input untuk fitur
crl_tot = st.number_input("circular.tot:")
dollar = st.number_input("dollar:")
bang = st.number_input("bang:")
money = st.number_input("money:")
n000 = st.number_input("n000:")
make = st.number_input("make:")

# Tombol untuk membuat prediksi
if st.button("Prediksi"):
    # Membuat DataFrame untuk input
    input_data = pd.DataFrame([[crl_tot, dollar, bang, money, n000, make]], columns=['crl.tot', 'dollar', 'bang', 'money', 'n000', 'make'])
    
    # Fit scaler pada data input (hanya dilakukan pertama kali)
    if 'X_train_scaled' not in st.session_state:
        X_train_scaled = scaler.fit_transform(input_data)  # Jika belum ada data latih
        st.session_state.X_train_scaled = X_train_scaled
    
    prediction = predict_spam(input_data)
    st.write("Hasil Prediksi: ", "Spam" if prediction[0][0] == 1 else "Not Spam")
