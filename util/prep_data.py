from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import string
import re


# =====================Prepocessing data tanpa menggunakan stopword======================
# Pisah setiap proses
def preprocess_data(text):
    # Lowercasing
    text = text.lower()
    
    # Remove punctuation
    separator = '|'
    hapus_tandabaca = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~1234567890'
    delete =str.maketrans(dict.fromkeys(hapus_tandabaca,' '))
    text = text.translate(delete)
    
    # Stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    # Tokenize
    tokens =  text.split()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    tokens = ' '.join(stemmed_tokens).split()
    
    return tokens
# ============================pemrosesan slang (mengubah bahasa gaul atau singkatan sesuai KBBI)==================================
def load_slang(slangpath):
    slang_dict = {}
    with open(slangpath, 'r', encoding='Utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split('\t')
                slang = parts[0]
                formal = parts[1] if len(parts) > 1 else ""
                slang_dict[slang] = formal
    return slang_dict

slang_file = "./Dataset/slang_indo.txt"
slng_dict = load_slang(slang_file)

def process_slang(text, slang_dict = slng_dict):
    words = text.split()
    processed_words = []

    for word in words:
         # Mengganti jika slang ditemukan, jika tidak, biarkan seperti itu
        processed_word = slang_dict.get(word.lower(), word) 
        processed_words.append(processed_word)

    processed_text = ' '.join(processed_words)
    return processed_text
# ==========================================Prep terpisah==========================================
def removepunc(text):
    # Lowercasing
    text = text.lower()
    # Remove punctuation
    separator = '|'
    hapus_tandabaca = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~1234567890'
    delete =str.maketrans(dict.fromkeys(hapus_tandabaca,' '))
    text = text.translate(delete)
    # Remove single letters
    text = re.sub(r'\b[a-zA-Z]\b', ' ', text)
    return text

def stemming(text):
    stemm = StemmerFactory()
    stemmer = stemm.create_stemmer()
    text = stemmer.stem(text)
    return text

def tokenize(text):
    # Tokenize
    text = text.split()
    return text