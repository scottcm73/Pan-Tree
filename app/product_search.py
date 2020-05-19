import os
import joblib
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
def pro_search(term):
    K = 10
    file_name1 = os.path.join("..", "Resources", "tfidf_pro.joblib")
    tfidf = joblib.load(file_name1)
    file_name3 = os.path.join("..", "Resources", "transformed_matrix_pro.pkl")
    with open(file_name3, "rb") as f:
        X = pickle.load(f)

    X_term = tfidf.transform([term])
    simularities = cosine_similarity(X_term, X)
    idxmax = np.argpartition(-simularities, K)
    return idxmax