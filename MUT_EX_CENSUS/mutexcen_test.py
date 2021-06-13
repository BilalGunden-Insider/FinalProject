# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 23:04:07 2021

@author: Aleyna Er
"""

#%% load model

import pickle
import sys

model = pickle.load(open(r"C:\Users\Bilal Günden\Desktop\MUT_EX_CENSUS\mutexcen_chromosome.pkl","rb"))

#%% read labels from csv and create list that contains labels (as df)

#import os
import pandas as pd
import glob 
import errno


path = r"C:\Users\Bilal Günden\Desktop\MUT_EX_CENSUS\label_encode_decode\*csv"
#os.chdir(path)

files = glob.glob(path)

unlabeled_features = []

for i in files:
     try: 
        df =  pd.DataFrame(pd.read_csv(i))
        unlabeled_features.append(df)
    
     except IOError as exc: 
        if exc.errno != errno.EISDIR: 
            raise 

#%% encode the inputs

userInput = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7]]

userInput_labeled = []

for i in range (len(userInput)):
    us_input = userInput[i]
    feature = unlabeled_features[i]
        #print(feature)
    for x in range(len(feature)): # feature df'i içinde dolaş
        var = feature["unlabeled"].values[x]
        if(us_input == var):
                #print(x)
            label = feature["labeled"].values[x]
            userInput_labeled.append(label)
            
        # if(us_input in feature):
        #     print("y")
        #     print(j)

#%% prediction phase

import numpy as np

test = np.array(userInput_labeled)
pred_label = model.predict(test.reshape(1,-1))
pred_label = pred_label[0]
        
#%% decode the predicted label and print prediction as output

chromosome_df = unlabeled_features[-1]

for i in range(len(chromosome_df)):
    chromosome_label = chromosome_df["labeled"].values[i]
    if(pred_label == chromosome_label):
        prediction = chromosome_df["unlabeled"].values[i]
        
#%% tahmin edilen hastalığın olasılığını bastırır

predPercent = model.predict_proba(test.reshape(1,-1))
predPercent = (predPercent.max())*100
predPercent = round(predPercent,2)
print("kromozom (chromosome ID) : {}".format(prediction)) ## hangi kromozom olduğunu bastırır
print("possibility : % {}".format(predPercent))

