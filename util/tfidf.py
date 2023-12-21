
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def tfidf_fit_transform(data):
    # Membuat objek CountVectorizer
    tf = TfidfVectorizer()
    # Mengubah data tokenized menjadi bentuk numerik dengan menggunakan fit_transform
    data_numerik = tf.fit_transform(data.apply(lambda x: " ".join(x)))
    return pd.DataFrame(data_numerik.toarray(), columns=tf.get_feature_names_out()), tf # type: ignore

def tfidf_transfrom(data, tfdidf):
    data_numerik = tfdidf.transform(data.apply(lambda x: " ".join(x)))
    return pd.DataFrame(data_numerik.toarray(), columns=tfdidf.get_feature_names_out())