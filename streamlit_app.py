import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Spam Classification Dataset")
st.write("Data Overview")

# Membaca dataset spam
df_spam = pd.read_csv("/df_spam = pd.read_csv("spam.csv", encoding="iso-8859-1")
", encoding="iso-8859-1")

# Menampilkan kolom untuk lebih memahami data
st.write("Dataset Columns: ", df_spam.columns.tolist())
st.write(df_spam)

# Misal terdapat kolom 'yesno' untuk klasifikasi spam vs ham
# Memfilter dataset berdasarkan kelas 'yesno' (spam atau ham)
df_filtered = df_spam[df_spam['yesno'].isin(['y', 'n'])]

# Menghitung jumlah kemunculan tiap kelas pada kolom 'yesno'
label_counts = df_filtered['yesno'].value_counts()

# Membuat DataFrame untuk visualisasi dan tabel
df_label_counts = pd.DataFrame(label_counts).reset_index()
df_label_counts.columns = ['yesno', 'Count']

# Mengubah nilai 'yesno' menjadi lebih deskriptif (spam -> Spam, ham -> Not Spam)
df_label_counts['yesno'] = df_label_counts['yesno'].replace({'spam': 'Spam', 'ham': 'Not Spam'})

# Menampilkan tabel jumlah tiap kelas 'yesno'
st.write("Class Counts Table")
st.dataframe(df_label_counts)

# Menampilkan dataset yang telah difilter
st.write("Filtered Dataset")
st.dataframe(df_filtered)

#
# Bar Chart untuk klasifikasi spam
#
st.title("Bar Chart of Spam Classification")
st.bar_chart(df_label_counts.set_index('yesno'))

st.markdown("---")