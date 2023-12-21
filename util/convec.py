from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def CVec_fit_transform(data):
    # Membuat objek CountVectorizer
    vectorizer = CountVectorizer()
    # Mengubah data tokenized menjadi bentuk numerik dengan menggunakan fit_transform
    data_numerik = vectorizer.fit_transform(data.apply(lambda x: " ".join(x)))
    return pd.DataFrame(data_numerik.toarray(), columns=vectorizer.get_feature_names_out()), vectorizer # type: ignore

def CVec_transfrom(data, countVec):
      data_numerik = countVec.transform(data.apply(lambda x: " ".join(x)))
      return pd.DataFrame(data_numerik.toarray(), columns=countVec.get_feature_names_out())