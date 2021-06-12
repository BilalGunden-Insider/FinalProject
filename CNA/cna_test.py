# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:05:52 2021

@author: Aleyna Er
"""
#%% load model

import pickle

model = pickle.load(open(r"C:\Users\Bilal Günden\Desktop\CNA\cna_primHist.pkl","rb"))

#%% read labels from csv and create list that contains labels (as df)

import pandas as pd
import glob 
import errno
import sys


path = r"C:\Users\Bilal Günden\Desktop\CNA\label_encode_decode\*csv"
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

userInput = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]]

userInput_labeled = []

for i in range (len(userInput)):
    us_input = userInput[i]
    #print(us_input)
    for j in range(len(unlabeled_features)-1): # feature seç
        feature = unlabeled_features[j]
        #print(feature)
        for x in range(len(feature)): # feature df'i içinde dolaş
            var = feature["unlabeled"].values[x]
            if(us_input == var):
                #print(x)
                label = feature["labeled"].values[x]
                userInput_labeled.append(label)

#%% prediction phase

import numpy as np

test = np.array(userInput_labeled)
pred_label = model.predict(test.reshape(1,-1))
pred_label = pred_label[0]

#%% decode the predicted label and print prediction as output

primHist_df = unlabeled_features[-1]

for i in range(len(primHist_df)):
    primHist_label = primHist_df["labeled"].values[i]
    if(pred_label == primHist_label):
        prediction = primHist_df["unlabeled"].values[i]

#%% tahmin edilen hastalığın olasılığını bastırır

predPercent = model.predict_proba(test.reshape(1,-1))
predPercent = (predPercent.max())*100
predPercent = round(predPercent,2)
print("Primary histology: {}".format(prediction)) ## hangi hastalık (primary histology) olduğunu bastırır
print("Possibility : % {}".format(predPercent))


