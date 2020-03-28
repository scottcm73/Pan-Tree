import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings
import pymysql
import os
import re
import datetime
import calendar
import random

USER = "datascm2_scott"
PASSWORD = "!8a{DKS/WATX9rr;-FFZ>4.}Uv#8`4sdsuX)Cjj,qVjqu,a6Q'k6Eg>Ezb`>%VvZ"
HOST = "162.241.193.35"
PORT = "3306"
DATABASE = "datascm2_home_inventory_db"

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", encoding="ISO 8859-1")



def insert_order(total_items_list, total_num_of_each, new_order_date, the_weekday, days_to_add, user_id):
    
    with engine.begin() as conn:

        this_cmd=f"INSERT INTO orders (user_id, order_dow, days_since_prior_order, order_date) VALUES('{user_id}', '{the_weekday}', '{days_to_add}', '{new_order_date}');"
    
        print(this_cmd)
    
        conn.execute(this_cmd)

        
        
        for total_items_list, total_num_of_each in zip(total_items_list, total_num_of_each):
            next_cmd=f"INSERT INTO order_products_prior (order_id, product_id, num_of_product )VALUES(LAST_INSERT_ID(),'{total_items_list}', '{total_num_of_each}');"
            conn.execute(next_cmd)

    
        final_cmd="COMMIT;"
        conn.execute(final_cmd)
        print("Success!")
    return


tables_list=["products"]
csv_list=["products_price.csv"] 

user_id=5

base_list=[39071, 13249, 4137, 1541, 
4149, 2619, 768, 1374, 1570, 13176, 11365, 3795,
941, 1969, 13517, 49276]
num_items_list=[1, 2, 3, 4, 5]
base_list_length=len(base_list)
base_num_items=np.random.choice(num_items_list, base_list_length, p=[.4, .2, .2, .1, .1])


list_beyond_base=[1153, 5933, 6632, 7390, 10371, 342, 1162, 1970, 3528, 4433, 
                28980, 32963, 28980, 12182, 2110, 5973, 14460, 39001, 33368, 
                39720, 387, 406, 6208, 6004, 6080, 21312, 31561, 47658, 47497, 
                14714, 1541, 4463, 11210, 15081, 23729, 45558, 1368, 1561, 3720, 
                4363, 5375, 5884, 6350, 41039, 44306, 5060, 7896, 9076, 6003, 5424,
                978, 1464, 10082]

the_date_str='2017-9-1'

the_date=datetime.datetime.strptime(the_date_str, '%Y-%m-%d').date()

base_dow=4  # Friday

print(the_date_str)

insert_order(base_list, base_num_items, the_date_str, base_dow, 0, user_id)



new_order_date=the_date
while new_order_date < datetime.date.today():
    day_add_list=[5, 6, 7, 8, 9]
    hour_of_day_list=[5, 6, 7, 8, 9]
    num_items_list=[1, 2, 3, 4, 5]
    day_add_random=np.random.choice(day_add_list, 1, p=[.2, .2, .2, .2, .2])


    days_to_add=int(str(day_add_random)[1:-1])
    new_order_date = new_order_date + datetime.timedelta(days=days_to_add)
    if new_order_date>datetime.date.today():
        pass
    else:

        the_weekday=new_order_date.weekday()

        total_num_items=np.random.choice([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
                                        20], 1, 
                                         p=[.0025, .0025, .0025, .0025, .005, .005, 
                                            .005, .005, .02, .03, .05, .07, 
                                            .1, .2, .4 ,.1])
   
        #Strip away brackets
        total_num_items=int(str(total_num_items)[1:-1])
        num_items_from_base_list=[5, 6, 7, 8, 9, 10, 11, 12, 13]
        random_num_items_from_base_list=np.random.choice(num_items_from_base_list, 1, p=[.025, .025, .1, .2, .3, .2, .1, .025, .025 ])
        random_num_items_from_base_list=int(str(random_num_items_from_base_list)[1:-1]) 
        if total_num_items>14:
            if random_num_items_from_base_list>total_num_items:
            #makes the number of random items from the base lits equal to the number of items
                random_num_items_from_base_list=total_num_items
            else:
                pass
        else:
            pass

        random_base=np.random.choice(base_list,random_num_items_from_base_list, replace=False)
        random_num_items_for_base_item=np.random.choice(num_items_list, random_num_items_from_base_list, p=[.4, .2, .2, .1, .1])

# Make list of random items beyond the base list.

        remaining_items=total_num_items-random_num_items_from_base_list
 
        if remaining_items>=1:
            random_remaining_items=np.random.choice(list_beyond_base, remaining_items, replace=False)
            num_items_for_each_remaining=np.random.choice(num_items_list, remaining_items, p=[.4, .2, .2, .1, .1])

        
              
            total_items_list=np.concatenate([random_base,random_remaining_items])


            total_num_of_each=np.concatenate([base_num_items, num_items_for_each_remaining])
        else:
            total_items_list=random_base
            total_num_of_each=random_num_items_for_base_item
        new_order_date_str=datetime.date.strftime(new_order_date, '%Y-%m-%d')
        insert_order(total_items_list, total_num_of_each, new_order_date_str, the_weekday, days_to_add, user_id)









    
