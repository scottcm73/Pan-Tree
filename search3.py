import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
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
    products_df = products_df.drop(['Unnamed: 5'], axis = 1)

    
    products_df['product_name']=products_df['product_name'].map(lambda x: re.sub(r'\W+', ' ', x))

    # Replace hyphens with spaces

    products_df['product_name']=products_df['product_name'].map(lambda x: re.sub(r'/-/g', ' ', x ))
    # Strip away numbers
    products_df['product_name']=products_df['product_name'].map(lambda x: re.sub(r'\d+', '', x ))
   
    
    products_df['product_name'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
    print(products_df.head())
    
    return products_df
products_wm_path = os.path.join('Resources', "products_wm.csv")
df = pd.read_csv(products_wm_path, index_col=False)
df2 = clean_product_data(df)
npdf2=df2.to_numpy()
print(npdf2)
X_text = df2["product_name"].values
cv = make_pipeline(
    CountVectorizer(
            ngram_range=(3, 7),
            analyzer="char"
        ),
    Normalizer()
)
cv.fit(X_text)
X = cv.transform(X_text)

file_name2 = os.path.join("Resources", "products_np.pkl")
with open(file_name2, 'wb') as f:
    this_np=pickle.dump(npdf2, f)


def search(term):
    K=5

 

    

    X_term = cv.transform([term])
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

   