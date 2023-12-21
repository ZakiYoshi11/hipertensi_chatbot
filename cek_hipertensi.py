from util.hipertensi import age, bmi, diabetes, jkelamin, kesehatan, kolesterol, konsumbuah, konsumsayur, olahraga, perokok
import pickle
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
import joblib

#  Model gaussian naive bayes
with open('savedata/data_hipertensi.csv', 'r') as f: # Data Prep
    df = pd.read_csv(f)
    
# Memanggil data dari file joblib
gaussianNB = joblib.load('savedata/gsnb.joblib')
            
def cek_hipertensi(input_text):
    input_text = input_text.lower()

    if '#cek' in input_text:
        # Memisahkan kata-kata yang tidak dimulai dengan 
        hasil = [word for word in input_text.split() if not word.startswith("#")]
        
        if len(hasil) == 11:
            try:
                # Menghasilkan hasil dalam variabel terpisah
                age_value = hasil[0]
                Sex_value = hasil[1]
                HighChol_value = hasil[2]
                tinggi_value = hasil[3]
                berat_value = hasil[4]
                Smoker_value = hasil[5]
                PhysActivity_value = hasil[6]
                PhysHlth_value = hasil[7]
                Fruits_value = hasil[8]
                Veggies_value = hasil[9]
                # GenHlth_value = hasil[10]
                Diabetes_value = hasil[10]
                
                # pemrosesan data
                age_input = age(age_value)
                sex_input = jkelamin(Sex_value)
                HighChol_input = kolesterol(HighChol_value)
                bmi_input = bmi(tinggi_value, berat_value)
                Smoker_input = perokok(Smoker_value)
                PhysActivity_input = olahraga(PhysActivity_value)
                PhysHlth_input = kesehatan(PhysHlth_value)
                Fruits_input = konsumbuah(Fruits_value)
                Veggies_input = konsumsayur(Veggies_value)
                # GenHlth_input = ratekesehatan(GenHlth_value)
                Diabetes_input = diabetes(Diabetes_value)

                cek_hipertensi = np.array([[age_input, sex_input, HighChol_input, bmi_input, Smoker_input,
                                            PhysActivity_input, PhysHlth_input, Fruits_input, Veggies_input,
                                            Diabetes_input]])
                prediction = gaussianNB.predict(cek_hipertensi)
                pred = prediction[0]
                
                # Mengembalikan hasil prediksi
                if pred == 1:
                    return "Anda memiliki penyakit hipertensi. Untuk proses penanganan sendiri yaitu sebagai berikut: \n1. Menurunkan berat badan dengan cara memperbanyak makanan sehat seperti buah-buahan dan sayur-sayuran \n2. Mengurangi konsumsi garam \n3. Rutin melakukan olahraga secara teratur selama 30 hari- 60 menit/hari. Minimal 3 hari/minggu \n4. mengurangi konsumsi alkohol \n5. Mengurangi Konsumsi Rokok \n- Jika ingin mengehtahui tingkat hipertensi kamu saat ini kamu dapat menginputkan tekanan darah kamu dengan format '#st (tekanan dara sistolik) #dt (tekanan dara diastolik) contohnya (#st 160 #dt 140)'."
                else:
                    return "selamat kamu tidak menderita hipertensi lo. jika ada yang ingin ditanyakan lagi silahkan kirim pesan kembali"
            except Exception:
                return "Pesan yang kamu masukkan tidak sesuai dengan format silahkan inputkan ulang"
        elif len(hasil) > 11:
            return 'pesan yang kamu masukkan melebihi pertanyaan, silahkan masukkan pesan ulang'
        else:
            return 'pesan yang kamu masukkan kurang dari pertanyaan yang ada, silahkan masukkan pesan ulang'
    else:
        return "pesan yang kamu masukkan tidak sesuai format, sertakan '#cek'"


# tes = '#cek 25 pria tidak 165 65 ya 0 tidak tidak 1 0'
# cek = cek_hipertensi(tes)
# print(cek)

      