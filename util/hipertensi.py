
def age(input_text):
    try:
        input_age = int(input_text)
        if input_age >= 80:
            return 13
        elif input_age >= 75:
            return 12
        elif input_age >= 70:
            return 11
        elif input_age >= 65:
            return 10
        elif input_age >= 60:
            return 9
        elif input_age >= 55:
            return 8
        elif input_age >= 50:
            return 7
        elif input_age >= 45:
            return 6
        elif input_age >= 40:
            return 5
        elif input_age >= 35:
            return 4
        elif input_age >= 30:
            return 3
        elif input_age >= 25:
            return 2
        elif input_age >= 18:
            return 1
        else:
            return 'Maaf, umur yang dimasukkan tidak valid.'
    except ValueError:
        return 'Maaf, umur harus berupa angka.'

# proses Jenis kelamin
def jkelamin(input_text):
      input_text = input_text.lower()
      sex_pria = ['laki-laki', 'laki laki', 'lelaki', 'laki', 'cowok', 'pria', 'cwok', 'lki']
      sex_perempuan = ['perempuan', 'wanita', 'cewek', 'permpuan', 'prmpuan', 'cwek', 'cwk', 'prmpuan']
      
      # Proses umur
      if input_text in sex_pria:
            return 1
      elif input_text in sex_perempuan:
            return 0
      else:
            return "Maaf, input tidak sesuai"
      
      
# proses data kolesterol
def kolesterol(input_text):
      pkl = ['ya', 'iya', 'y', 'iy', 'yap', 'yaps', 'yoi', 'betul', 'tul']
      nkl = ['tidak', 'ngga', 'tdk', 'nggak', 'ngg']
    
      input_text = input_text.lower().strip()  
      if input_text in pkl:
            return 1
      elif input_text in nkl:
            return 0
      else:
            return "Maaf, input tidak sesuai"
      
# Proses data BMI dari tinggi dan berat badan
def bmi(tinggi, berat):
      try:
            height = float(tinggi)
            brt = float(berat)
            # Mengubah tinggi dari cm ke m
            height = height / 100

            # Menghitung BMI
            bmi = brt / (height * height)
            if bmi < 18.5:
                  return 1
            elif  bmi <= 24.9:
                  return 2
            elif  bmi <= 29.9:
                  return 3
            elif bmi>= 30:
                  return 4
            else:
                  return "belum ada inputan atau inputan yang kamu masukkan tidaklah sesuai"
      except Exception:
            return  "Inputan masih kosong atau tidak sesuai format"

# proses data perokok
def perokok(input_text):
      pkl = ['ya', 'iya', 'y', 'iy', 'yap', 'yaps', 'yoi']
      nkl = ['tidak', 'ngga', 'tdk', 'nggak', 'ngg']
    
      input_text = input_text.lower().strip()  
      if input_text in pkl:
            return 1
      elif input_text in nkl:
            return 0
      else:
            return "Maaf, input tidak sesuai"
      
# proses data olahraga
def olahraga(input_text):
      pkl = ['ya', 'iya', 'y', 'iy', 'yap', 'yaps', 'yoi']
      nkl = ['tidak', 'ngga', 'tdk', 'nggak', 'ngg']
    
      input_text = input_text.lower().strip()  
      if input_text in pkl:
            return 1
      elif input_text in nkl:
            return 0
      else:
            return "Maaf, input tidak sesuai"
      

# penyakit yang di alami jika ada selama 30 hari terakhir
def kesehatan (input_text):
      pi = float(input_text)
      if 0 <= pi <= 30:
            return pi
      else:
            return "Maaf, input tidak sesuai"

# proses data mengkonsumsi buah
def konsumbuah(input_text):
      pkl = ['ya', 'iya', 'y', 'iy', 'yap', 'yaps', 'yoi']
      nkl = ['tidak', 'ngga', 'tdk', 'nggak', 'ngg']
    
      input_text = input_text.lower().strip()  
      if input_text in pkl:
            return 1
      elif input_text in nkl:
            return 0
      else:
            return "Maaf, input tidak sesuai"
      
 # proses data mengkonsumsi sayur
def konsumsayur(input_text):
      pkl = ['ya', 'iya', 'y', 'iy', 'yap', 'yaps', 'yoi']
      nkl = ['tidak', 'ngga', 'tdk', 'nggak', 'ngg']
    
      input_text = input_text.lower().strip()  
      if input_text in pkl:
            return 1
      elif input_text in nkl:
            return 0
      else:
            return "Maaf, input tidak sesuai"     
 
# proses data penderita diabetes
def diabetes(input_text):
      pkl = ['ya', 'iya', 'y', 'iy', 'yap', 'yaps', 'yoi']
      nkl = ['tidak', 'ngga', 'tdk', 'nggak', 'ngg']
    
      input_text = input_text.lower().strip()  
      if input_text in pkl:
            return 1
      elif input_text in nkl:
            return 0
      else:
            return "Maaf, input tidak sesuai" 
       