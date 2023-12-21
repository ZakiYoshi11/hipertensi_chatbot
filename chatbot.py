import pandas as pd
import pickle
import json
from util.model import MultinomialNaiveBayes
from util.prep_data import preprocess_data, process_slang
from util.convec import CVec_transfrom
import joblib

# =============================================
# Load Data tensi_skripsi
# =============================================
datajson= "./Dataset/Tensi_skripsi.json"
with open(datajson, 'r') as file:
        data = json.load(file)

# =============================================
# Read dile data preprocesing dan data X
# =============================================
# with open('savedata/data_prep_new.csv', 'r') as f: # Data Prep
#       df = pd.read_csv(f)
      
# =============================================
# Load data CVec.pkl
# =============================================
with open('./savedata/CVec_new.pkl', 'rb') as f:
    CVec = pickle.load(f)

model_filename = "savedata/naive_bayes_model_new.pkl"
naive_bayes =  joblib.load(model_filename)

# ==============================================
# menerima inputan dan memberikan respon 
# berdasarkan model yang telah dilatih
# ==============================================
def get_response(question):
      
    # Melakukan preprocessing pada input yang akan diuji
    question = process_slang(question)
    question = preprocess_data(question)
    
    # Mengubah input yang akan diuji menjadi bentuk yang dapat digunakan oleh model Multinomial Naive Bayes
    qustion = CVec_transfrom(pd.Series([question]), CVec)

    # Mengklasifikasikan input berdasarkan model yang telah dibuat
    pred = naive_bayes.predict_class(qustion.to_numpy())
    prob = naive_bayes.predict_prob(qustion.to_numpy())

    # Mengambil hasil klasifikasi (kelas prediksi)
    predicted_class = pred[0]
    
    # Mendapatkan jawaban berdasarkan kelas prediksi
    output_jawaban = None
    threshold = 0.7

    # Mencari jawaban yang sesuai berdasarkan probabilitas prediksi
    for i, probabilities in enumerate(prob):
        max_probability = probabilities.max()
        if max_probability >= threshold:
            for intent in data["intents"]:
                if intent["tag"] == predicted_class:
                    output_jawaban = intent["responses"]
                    return output_jawaban  # Mengembalikan jawaban langsung di dalam fungsi
        else:
            output_jawaban = "Maaf, kami tidak memahami yang Anda sampaikan. Silakan masukkan pertanyaan atau pernyataan lainnya."
    return output_jawaban
        
    
        
# # Contoh penggunaan chatbot
# input_question = "cek hipertensi"
# response = get_response(input_question)
# print("Chatbot: ", response)