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

def clean_product_data(df):
    
    products_df = df
  

    #Takes out most punctuation
    products_df['product_name']=products_df['product_name'].map(lambda x: re.sub(r'\W+', ' ', x))

    # Replace hyphens with spaces

    products_df['product_name']=products_df['product_name'].map(lambda x: re.sub(r'/-/g', ' ', x ))
    # Strip away numbers
    products_df['product_name']=products_df['product_name'].map(lambda x: re.sub(r'\d+', '', x ))
   
    # Take out stopwords
    products_df['product_name'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
    print(products_df.head())
    
    return products_df
products_wm_path = os.path.join('Resources', "join_t_tables_wad.csv")
df = pd.read_csv(products_wm_path, index_col=False)
df2 = clean_product_data(df)
npdf2=df2.to_numpy()
print(npdf2)
X_text = df2["product_name"].values
tfidf = TfidfVectorizer(ngram_range=(3, 7),
            analyzer="char")


tfidf.fit(X_text)
X = tfidf.transform(X_text)
file_name1 = os.path.join("Resources", "tfidf.pkl")
with open(file_name1, 'wb') as f:
    pickle.dump(tfidf, f)

file_name2 = os.path.join("Resources", "products_np.pkl")
with open(file_name2, 'wb') as f:
    pickle.dump(npdf2, f)

file_name3 = os.path.join("Resources", "transformed_matrix.pkl")
with open(file_name3, 'wb') as f:
    pickle.dump(X, f)




def search(term):
    K=5

    file_name1 = os.path.join("Resources", "tfidf.pkl")
    with open(file_name1, 'rb') as f:
        tfidf=pickle.load(f)



    file_name3 = os.path.join("Resources", "transformed_matrix.pkl")
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

   