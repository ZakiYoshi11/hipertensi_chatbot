import json

def import_json(file_name):
    with open(file_name, 'r') as file:
        content = json.load(file)
    return content

def detect_hypertension(input_text):
      hipertensi_derajat1 =import_json('dataset/hipertensi_derajat1.json')
      hipertensi_derajat2 =import_json('dataset/hipertensi_derajat2.json')
      hipertensi_derajat3 =import_json('dataset/hipertensi_derajat3.json')
      hipertensi_terisolisasi =import_json('dataset/hipertensi_terisolisasi.json')

      input_text = input_text.lower().strip()

      # Cek apakah input mengandung "#st" dan "#dt"
      if "#st" in input_text and "#dt" in input_text:
            try:
                  systolic_pressure = int(input_text.split("#st")[1].split("#dt")[0].strip())
                  diastolic_pressure = int(input_text.split("#dt")[1].strip())
            except ValueError:
                  return "Tekanan sistolik atau diastolik tidak valid. Mohon masukkan angka."

            # Klasifikasi berdasarkan tekanan sistolik dan diastolik
            if systolic_pressure <=90 and diastolic_pressure <=60:
                  return "Tekanan darah kakak terlalu rendah nih"
            if systolic_pressure >= 140 and diastolic_pressure < 90:
                  return hipertensi_terisolisasi
            elif systolic_pressure <120 and diastolic_pressure <90:
                  return "Tekanan darah kamu optimal normal, jaga kesehatan terus ya!!"
            elif systolic_pressure <= 120 and diastolic_pressure < 80:
                  return "Tekanan darah kamu Tekanan darah normal, jaga kesehatan terus ya!!."
            elif systolic_pressure < 130 and diastolic_pressure < 85:
                  return "Tekanan darah kamu Normal tinggi, jaga kesehatan terus ya!!."
            elif systolic_pressure < 140 and diastolic_pressure < 90:
                  return hipertensi_derajat1
            elif systolic_pressure < 160 and diastolic_pressure < 100:
                  return hipertensi_derajat2
            else:
                  return hipertensi_derajat3
      else:
            return "Mohon masukkan tekanan darah yang valid (#st dan #dt)."
