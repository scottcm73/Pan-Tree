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
import re
import csv

def clean_product_data(product_list2):
    pro_list_copy=product_list2
   
    for row in pro_list_copy:
        #Takes out most punctuation
        row[1]=row[1].replace('\W+', ' ')
    
        row[1]=row[1].replace('\d+', '')
        row[1]=row[1].replace(r'/-/g', ' ')
    # Strip away numbers
        row[1]=row[1].replace(r'\d+', '')
        ' '.join([word for word in row[1].split() if word not in (stopwords)])


    
    return pro_list_copy
def get_data():
    the_invent_list=[]
    products_wad_path = os.path.join('Resources', "join_t_tables_wad.csv")
    with open(products_wad_path, "r") as this_csv_file:
        this_csv_reader = csv.reader(this_csv_file, delimiter=",")
        header=next(this_csv_reader)
        for line in this_csv_reader:
            the_invent_list.append(line)




    return the_invent_list
# Numpy array column with product_name






#Plan to do search on the fly so no pickled files!!!
# file_name1 = os.path.join("Resources", "tfidf.pkl")
# with open(file_name1, 'wb') as f:
#     pickle.dump(tfidf, f)

# file_name2 = os.path.join("Resources", "products_np.pkl")
# with open(file_name2, 'wb') as f:
#     pickle.dump(npdf2, f)

# file_name3 = os.path.join("Resources", "transformed_matrix.pkl")
# with open(file_name3, 'wb') as f:
#     pickle.dump(X, f)

def search(term, tfidf, X):
    K=10

    X_term = tfidf.transform([term])
    simularities = cosine_similarity(X_term, X)
    idxmax = np.argpartition(-simularities, K)  
    return idxmax

def start_search(term):



    invent=get_data()
    the_invent_list=clean_product_data(invent)
    npdf2=np.array(the_invent_list)
    X_text = npdf2[:, 1]
    tfidf = TfidfVectorizer(ngram_range=(3, 7),
        analyzer="char")

    tfidf.fit(X_text)
    X = tfidf.transform(X_text)
    idx=search(term, tfidf, X)
    print(idx)

    idxs=idx[0]
    for x in range(5):
        print(npdf2[idxs[x]])
    return idxs


   