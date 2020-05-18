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

        print(product_list2)
       
        
        pro_json=json.dumps([{"id": b[0], "amount_bought": b[1], "amount_left": b[2], "use_item": b[3], "product_id": b[4], "product_name":b[5]} for b in product_list2])
        print(pro_json)        
        return pro_json

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

                if product_array2[x, 4]==product_array[y, 0]:
                    no_need=True
                    return no_need
                if product_array2[x, 5]== product_array[y, 1]:
                    no_need=True
                    return no_need

                if product_array2[x, 1]==term:
                    no_need=True
                    return no_need
    


        return no_need