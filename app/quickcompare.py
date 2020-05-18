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
import joblib
import csv
import json

class recommend():

    def __init__(self):
        return
    
    def make_json(self, product_list, product_list2):
        self.product_list = product_list
        self.product_list2 = product_list2
        print(product_list)
        print(product_list2)
        
        
        in_pro_json=json.dumps([{"order_date": b[2], "product_name": b[3], "product_id": b[5], "quantity": b[6], "q_left": b[7], "trash":b[8]} for b in product_list2])
        print(in_pro_json)  
        self.in_pro_json=in_pro_json 
        pro_json=json.dumps([{"product_id": b[0], "product_name": b[1], "price": b[4]} for b in product_list])
        self.pro_json=pro_json
        return in_pro_json

    def recommender(self, product_array, product_array2, term, K):
        
        return product_array

   
    def compare(self, product_array, product_array2, term, K):
        self.product_array=product_array
        self.product_array2=product_array2
        print("product list")


        no_need=False
        print("product_array")
        print(product_array)
        print("product_array2")
        print(product_array2)
        print(product_array2[0,5])
        for x in range(K):
            for y in range(K):

                if product_array2[x, 3]==product_array[y, 1]:
                    no_need=True
                    return no_need
                if product_array2[x, 6]== product_array[y, 0]:
                    no_need=True
                    return no_need

                if product_array2[x, 3]==term:
                    no_need=True
                    return no_need
    


        return no_need