import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.datasets import dump_svmlight_file
from stopwds import stopwords
import pandas as pd 
import os
import pickle






def search(term):
    K=5

    file_name1 = os.path.join("Resources", "tfidf_pro.pkl")
    with open(file_name1, 'rb') as f:
        tfidf=pickle.load(f)



    file_name3 = os.path.join("Resources", "transformed_matrix_pro.pkl")
    with open(file_name3, 'rb') as f:
        X = pickle.load(f)

    

    X_term = tfidf.transform([term])
    simularities = cosine_similarity(X_term, X)
    idxmax = np.argpartition(-simularities, K)  
    return idxmax

if __name__ == "__main__":
    term = "choclate cooies mnt"
    file_name2 = os.path.join("Resources", "products_np.pkl")
    with open(file_name2, 'rb') as f:
        this_np=pickle.load(f)

    print(this_np)
    idx=search(term)
    print(idx)

    idxs=idx[0]
    for x in range(5):
        print(this_np[idxs[x]])