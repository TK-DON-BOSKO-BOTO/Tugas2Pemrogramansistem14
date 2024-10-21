import streamlit as st
import pandas as pd

# Fungsi untuk memuat dataset
def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        return None

# Judul aplikasi
st.title("Visualisasi Kolom Dataset SPAM")

# Input untuk memasukkan dataset
uploaded_file = st.file_uploader("spam.csv", type=["csv"])

# Memuat data
df = load_data(uploaded_file)

if df is not None:
    # Menampilkan tabel data untuk referensi
    st.write("Dataframe SPAM:")
    st.dataframe(df.head())

    # Input untuk memilih jenis grafik
    chart_type = st.selectbox("Pilih jenis grafik", ["Line Chart", "Bar Chart", "Area Chart"])

    # Input untuk memilih kolom
    columns = st.multiselect("Pilih kolom yang ingin ditampilkan dari dataset SPAM", df.columns)

    # Menampilkan grafik per kolom yang dipilih
    for column in columns:
        st.write(f"Grafik untuk kolom: {column} dari dataset SPAM")
        
        if chart_type == "Line Chart":
            st.line_chart(df[[column]])
        elif chart_type == "Bar Chart":
            st.bar_chart(df[[column]])
        elif chart_type == "Area Chart":
            st.area_chart(df[[column]])
else:
    st.write("spam.csv")
