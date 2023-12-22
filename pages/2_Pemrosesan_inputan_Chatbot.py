import streamlit as st
import pandas as pd
from util.prep_data import process_slang, removepunc, stemming, tokenize, preprocess_data
from util.convec import CVec_transfrom
import pickle
from util.model import MultinomialNaiveBayes
import json
import joblib


# ----------Import Data--------------
with open('./savedata/CVec_new.pkl', 'rb') as f:
    CVec = pickle.load(f)
    
# Import data hasil counvec 
with open('./savedata/X_conv_new.csv', 'r') as f: # Data X
      X = pd.read_csv(f)
      
datajson= "./Dataset/Tensi_skripsi.json"
with open(datajson, 'r') as file:
        data = json.load(file)
        
with open('./savedata/data_prep_new.csv', 'r') as f: # Data Prep
      df = pd.read_csv(f)
      
model = MultinomialNaiveBayes()
# membuat varabel "y" yang berisikan kategori dari data
y = df['kategori']

# ==============================================
# Melatih Model
# ==============================================
model.fit(X, y)

# model_filename = "savedata/naive_bayes_model_new.pkl"
# model =  joblib.load(model_filename)

# ===============SETUP===============    
# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style>
# """
st.set_page_config(
    page_title="Demo Chatbot",
    page_icon="⛑"
)
# st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Visualisasi dan Pemrosesan Inputan Chatbot")
st.sidebar.success("Pilih Halaman Di Atas")
st.write("---")
 #---Pemrosesan teks atau kata---
#  input pesan
input_text = st.text_input("Tuliskan pesan kamu:")
st.subheader("Text preprocessing/pemrosesan text")

# Menampilkan Kalimat original
st.text('Kalimat atau kata sebelum di proses:')
with st.expander("Klik"):
    st.write(input_text)

# Mengubah kata gaul atau 
slang = process_slang(input_text)
st.text('Mengubah kata gaul atau singkatan menjadi kata baku:')
with st.expander("Klik"):
    st.write(slang)

# Normalisasi kata seperti menghapus kata yang tidak diperlukan
cleansing = removepunc(slang)
st.text('Proses Normalisasi Kalimat:')
with st.expander("Klik"):
    st.write(cleansing)
    
# Memisahkan kata (Tokenize)
token = tokenize(cleansing)
st.text('Memisahkan kata (Tokenize):')
with st.expander("Klik"):
    st.write(token)
    
# Menghapus kata yang tidak baku atau tidak sesuai dengan KBBI
stemm = preprocess_data(slang)
st.text('Mengubah kata yang tidak baku menjadi kata baku:')
with st.expander("Klik"):
    st.write(stemm)
    
# Menghapus kata yang tidak baku atau tidak sesuai dengan KBBI
conv = CVec_transfrom(pd.Series([stemm]), CVec)
st.text('Mengubah setiap kata agar dapat dipahami oleh sistem menggunakan Counvectorizer:')
with st.expander("Klik"):
    st.write(conv)
    
st.write("---")
st.subheader("Prediction dan Probabilitas Menggunakan Multinomial Naive Bayes")

# Mengklasifikasikan input berdasarkan model yang telah dibuat
pred = model.predict_class(conv.to_numpy())
# Mengambil hasil klasifikasi (kelas prediksi)
predicted_class = pred[0]
st.text('Class atau kategori yang di prediksi:')
with st.expander("Klik"):
    st.write(predicted_class)
    
prob = model.predict_prob(conv.to_numpy())
prob_class = prob[0]
st.text('Probabilitas hasil prediksi:')
with st.expander("Klik"):
    st.write(prob_class)

st.write("Jawaban:")
# Mendapatkan jawaban berdasarkan kelas prediksi
output_jawaban = None
threshold = 0.7
try:
    # Mencari jawaban yang sesuai berdasarkan probabilitas prediksi
    for i, probabilities in enumerate(prob):
        max_probability = probabilities.max()
        if max_probability > threshold:
            for intent in data["intents"]:
                if intent["tag"] == predicted_class:
                    output_jawaban = intent["responses"]
                    st.write(output_jawaban)
        else:
            # Inisialisasi pesan jika probabilitas di bawah threshold
            pesan_probabilitas_rendah = f"tidak dapat menampilkan jawaban karena probabilitas dari kategori atau class dibawah {threshold*100}%. adapun probabilitas dari class ({predicted_class}) yaitu {max_probability*100}%"
            st.write(pesan_probabilitas_rendah)
except Exception:
    error =  "Belum Pesan yang di inputkan"
    st.write(error)
