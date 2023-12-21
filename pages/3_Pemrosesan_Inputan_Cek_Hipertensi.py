import streamlit as st
from util.hipertensi import age, bmi, diabetes, jkelamin, kesehatan, kolesterol, konsumbuah, konsumsayur, olahraga, perokok
import pickle
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
import joblib

#  Model gaussian naive bayes
with open('./savedata/data_hipertensi.csv', 'r') as f: # Data Prep
    df = pd.read_csv(f)

# Memanggil data dari file joblib
gaussianNB = joblib.load('savedata/gsnb.joblib')

# ===============SETUP===============
# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style>
# """
st.set_page_config(
    page_title="Tensibot",
    page_icon="⛑"
)
# st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("About Hypertension Prediction")
st.sidebar.success("Pilih Halaman Di Atas")
st.write('---')


# ================hypertension prediction==============
st.subheader("Pertanyaan Untuk Predict Hipertensi")

age_value = st.number_input("Berapa Umur kamu saat ini?")

Sex_value = st.selectbox("Apakah kamu laki-laki atau perempuan?", ['Klik',"laki-laki", "Perempuan"])

HighChol_value = st.selectbox("Apakah Kolesterol anda tinggi?", ['Klik',"Iya", "Tidak"])

tinggi_value = st.number_input("Berapa Tinggi badan kamu(cm)?")

berat_value = st.number_input("Berapa berat badan kamu (Kg)?")

Smoker_value = st.selectbox("Apakah kamu merokok minimal 5 bungkus hingga saat ini", ['Klik',"iya", "tidak"])

PhysActivity_value = st.selectbox("Apakah kamu melakukan aktivitas fisik selain bekerja", ['Klik',"Iya", "Tidak"])

PhysHlth_value = st.number_input("Apakah anda mengalami atau mengidap penyakit dalam 30 hari terakhir ini, jika ya isi berapa  hari (1-30)?  (jika tidak maka isi (0))")

Fruits_value = st.selectbox("Apakah kamu mengkonsumsi buah setidaknya satu kali sehari?", ['Klik',"Iya", "Tidak"])

Veggies_value = st.selectbox("Apakah Kamu mengkonsumsi Sayur setidaknya satu kali sehari?", ['Klik',"Iya", "Tidak"])

Diabetes_value = st.selectbox("Apakah kamu mengalami diabetes", ['Klik',"Iya", "Tidak"])

# ================Data Preprocessing/pemrosesan data==============
st.write('---')
st.subheader("Data preprocessing atau pengolahan data inputan")
st.write('---')


age_input = age(age_value)
st.text('Konversi umur')
with st.expander("Klik"):
    st.write(age_input)
    
sex_input = jkelamin(Sex_value)
st.text('Konversi Jenis kelamin')
with st.expander("Klik"):
    st.write(sex_input)
    
HighChol_input = kolesterol(HighChol_value)
st.text('Konversi Kolesterol')
with st.expander("Klik"):
    st.write(HighChol_input)
    
bmi_input = bmi(tinggi_value, berat_value)
st.text('Pemrosesan tinggi badan dan berat badan untuk BMI')
with st.expander("Klik"):
    st.write(bmi_input)
    
Smoker_input = perokok(Smoker_value)
st.text('Konversi Perokok atau tidak')
with st.expander("Klik"):
    st.write(Smoker_input)
    
PhysActivity_input = olahraga(PhysActivity_value)
st.text('Konversi Aktifitas fisik')
with st.expander("Klik"):
    st.write(PhysActivity_input)
    
PhysHlth_input = kesehatan(PhysHlth_value)
st.text('Konversi Konidisi kesahatan selama 30 hari terakhir')
with st.expander("Klik"):
    st.write(PhysHlth_input)
    
Fruits_input = konsumbuah(Fruits_value)
st.text('Konversi konsumsi buah atau tidak minimal 1 kali sehari')
with st.expander("Klik"):
    st.write(Fruits_input)
    
Veggies_input = konsumsayur(Veggies_value)
st.text('Konversi konsumsi sayur atau tidak minimal 1 kali sehari')
with st.expander("Klik"):
    st.write(Veggies_input)
    
Diabetes_input = diabetes(Diabetes_value)
st.text('Konversi apakah mengalami diabetes atau tidak')
with st.expander("Klik"):
    st.write(Diabetes_input)
    

try:
    cek_hipertensi = np.array([[age_input, sex_input, HighChol_input, bmi_input, Smoker_input,
                                PhysActivity_input, PhysHlth_input, Fruits_input, Veggies_input,
                                Diabetes_input]])
    # Membuat dataframe dari array numpy
    df_cek_hipertensi = pd.DataFrame(cek_hipertensi, columns=['Age', 'Sex', 'HighChol', 'BMI', 'Smoker',
                                                                    'PhysActivity', 'PhysHlth', 'Fruits', 'Veggies',
                                                                    'Diabetes'])
    st.text('Hasil Pemrosesan Data Inputan Baru')
    st.write(df_cek_hipertensi)

    st.write('Ouput:')
    prediction = gaussianNB.predict(cek_hipertensi)
    probabilitas = gaussianNB.predict_proba(cek_hipertensi)
    Hight_prob = probabilitas.max(axis=1)
    pred = prediction[0]
    prob = Hight_prob[0]
    
   
    

    # Mengembalikan hasil prediksi
    if pred == 1:
        post_hipertensi = "Anda memiliki penyakit hipertensi. Jika Anda memiliki pertanyaan lebih lanjut, silakan tanyakan."
        st.write(post_hipertensi)
    else:
        no_hipertensi = "selamat kamu tidak menderita hipertensi lo. jika ada yang ingin ditanyakan lagi silahkan kirim pesan kembali"
        st.write(no_hipertensi)
except Exception:
    error =  "Pesan yang kamu masukkan tidak sesuai dengan format atau belum ada pesan yang diinputkan."
    st.write(error)

try:
    #  Menampilkan hasil prediksi
    st.text('Hasil Prediksi dan Probabilitas:')
    st.write(pred)
    
    if pred == 0.0:
        # Menampilkan Probabilitas 
        st.text('Prediksi:')
        st.write(probabilitas)
        st.text(f'Dari proses diagnosa hipertensi menunjukkan hasil prediksi  yaitu {pred} dengan probabilitas {prob}. Berarti tidak mengalami mengalami hipertensi')
    else:
        # Menampilkan Probabilitas 
        st.text('probabilitas:')
        st.write(probabilitas)
        st.text(f'Dari proses diagnosa hipertensi menunjukkan hasil prediksi  yaitu {pred} dengan probabilitas {prob}. Berarti mengalami mengalami hipertensi')
except Exception:
    error =  "Belum ada proses prediksi dan Probabilitas karena data belum ada yang diinputkan"
    st.write(error)