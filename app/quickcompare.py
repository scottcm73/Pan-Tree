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
from itertools import filterfalse
class recommend():

    def __init__(self):
        return
    


    def compare(self, product_list, product_list2, term, K):
        self.product_list=product_list
        self.product_list2=product_list2
        print("product list")

        self.term=term
        no_need=False

        for x in product_list:
            for y in product_list2:
                #same product_id
                if  x[0]==y[3]:
                    no_need=True
                    self.no_need=no_need
                    return no_need
                #same product_name
                if  x[1]== y[1]:
                    no_need=True
                    self.no_need=no_need
                    return no_need

                if y[3]==term:
                    no_need=True
                    self.no_need=no_need
                    return no_need
                

    

        self.no_need=no_need
        return no_need

    def recommender(self, product_list, product_list2, term):
        self.product_list=product_list
        self.product_list2=product_list2
        pro_list_copy=[]
        
        if self.no_need:

            
        #     
            for y in product_list2:
                for x in product_list:
                    #same product_id
                    if  (x[0]!=y[3]) and (x[1]!=y[1]) and (y[3]!=term) and (term not in y[1] or y[7]!=x[4]):
                        pro_list_copy.append(x)
            
            pro_list_copy2 = []
            for a in pro_list_copy:
                if a not in pro_list_copy2:
                    pro_list_copy2.append(a)
                        
            pro_list_copy=pro_list_copy2
        else:
            pro_list_copy=product_list
        print('pro_list_copy')           # if my_pro_json[row2]['product_name'].count(term)>=1:
        print(len(pro_list_copy))           #     pro_json_copy.pop(row2)
        return pro_list_copy

        